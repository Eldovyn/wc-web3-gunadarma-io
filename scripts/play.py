import os
import json
import time
import requests
import click
from dotenv import load_dotenv
from ape import accounts, project, networks

load_dotenv()

def upload_file_to_pinata(file_path, metadata_name):
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    headers = {
        "pinata_api_key": os.getenv("VITE_PINATA_API_KEY") or os.getenv("PINATA_API_KEY"),
        "pinata_secret_api_key": os.getenv("VITE_PINATA_SECRET_API_KEY") or os.getenv("PINATA_SECRET_API_KEY"),
    }
    with open(file_path, "rb") as f:
        files = {"file": f}
        data = {"pinataMetadata": json.dumps({"name": metadata_name})}
        response = requests.post(url, headers=headers, files=files, data=data)
        response.raise_for_status()
        return response.json()["IpfsHash"]

def upload_json_to_pinata(json_data, metadata_name):
    url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
    headers = {
        "pinata_api_key": os.getenv("VITE_PINATA_API_KEY") or os.getenv("PINATA_API_KEY"),
        "pinata_secret_api_key": os.getenv("VITE_PINATA_SECRET_API_KEY") or os.getenv("PINATA_SECRET_API_KEY"),
        "Content-Type": "application/json"
    }
    data = {
        "pinataContent": json_data,
        "pinataMetadata": {"name": metadata_name}
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["IpfsHash"]

@click.command()
@click.argument("account_name")
@click.argument("guess_number", type=int)
@click.option("--address", default=None, help="Alamat (Address) dari kontrak TebakAngka (Game) yang sudah dideploy")
@click.option("--network", default="ethereum:sepolia:node", help="Network specifier")
def cli(account_name, guess_number, address, network):
    if not (1 <= guess_number <= 5):
        print("Error: Tebakan angka harus antara 1 sampai 5!")
        return

    if not address:
        address = os.getenv("TEBAK_ANGKA_ADDRESS")
        if not address or not address.startswith("0x") or len(address) != 42:
            print("Error: Game address must be provided via --address or set as a valid TEBAK_ANGKA_ADDRESS in .env!")
            return

    with networks.parse_network_choice(network) as provider:
        print(f"Active Network: {provider.network.name}")
        
        try:
            # Memuat akun pemain
            player = accounts.load(account_name)
            player.set_autosign(True)
        except KeyError:
            print(f"Error: Account '{account_name}' is not found in Ape.")
            return

        print(f"Bermain menggunakan akun: {player.address}")
        
        # Memuat (load) kontrak Game yang sudah dideploy ke jaringan
        game = project.TebakAngka.at(address)
        
        print(f"Menebak angka {guess_number} ke kontrak {game.address}...")
        
        try:
            print("Mengunggah gambar dan metadata ke Pinata...")
            win_image_path = "images/win.png"
            lose_image_path = "images/lose.png"
            
            win_image_hash = upload_file_to_pinata(win_image_path, "TebakAngka_Win_Image")
            lose_image_hash = upload_file_to_pinata(lose_image_path, "TebakAngka_Lose_Image")
            
            win_metadata = {
                "name": "TebakAngka Winner NFT",
                "description": f"NFT eksklusif pemenang game TebakAngka! Pemain menebak angka {guess_number} dengan benar.",
                "image": f"https://gateway.pinata.cloud/ipfs/{win_image_hash}",
                "attributes": [
                    {"trait_type": "Tebakan", "value": guess_number},
                    {"trait_type": "Status", "value": "Menang"},
                    {"trait_type": "Game", "value": "TebakAngka"}
                ]
            }
            
            lose_metadata = {
                "name": "TebakAngka Loser NFT",
                "description": f"NFT eksklusif partisipan game TebakAngka. Pemain menebak angka {guess_number} namun kurang beruntung.",
                "image": f"https://gateway.pinata.cloud/ipfs/{lose_image_hash}",
                "attributes": [
                    {"trait_type": "Tebakan", "value": guess_number},
                    {"trait_type": "Status", "value": "Kalah"},
                    {"trait_type": "Game", "value": "TebakAngka"}
                ]
            }
            
            win_metadata_hash = upload_json_to_pinata(win_metadata, f"TebakAngka_Winner_{int(time.time())}.json")
            lose_metadata_hash = upload_json_to_pinata(lose_metadata, f"TebakAngka_Loser_{int(time.time())}.json")
            
            win_uri = f"https://gateway.pinata.cloud/ipfs/{win_metadata_hash}"
            lose_uri = f"https://gateway.pinata.cloud/ipfs/{lose_metadata_hash}"
            print(f"Metadata berhasil diunggah! Win URI: {win_uri}")

            # Memanggil fungsi guess pada smart contract
            # Set gas_limit manual untuk mencegah Out of Gas jika pemain menang
            tx = game.guess(guess_number, win_uri, lose_uri, sender=player, gas_limit=800000)
            print(f"\nTransaksi berhasil! Hash: {tx.txn_hash}")
            
            # Membaca log/event GuessMode untuk melihat hasilnya
            logs = list(tx.decode_logs(game.GuessMode))
            if logs:
                event = logs[0]
                print("\n--- HASIL GAME ---")
                print(f"Tebakan Anda: {event.guess}")
                print(f"Angka yang Benar: {event.correctNumber}")
                
                if event.won:
                    print("🎉 SELAMAT! Tebakan Anda BENAR!")
                    print("🎁 Anda mendapatkan 10 Token TebakAngkaCoin dan 1 TebakAngkaNFT.")
                else:
                    print("😢 Sayang sekali tebakan Anda SALAH. Coba lagi!")
                print("------------------")
            else:
                print("Event GuessMode tidak ditemukan di transaksi ini.")
                
        except Exception as e:
            print(f"Error saat mengeksekusi transaksi: {e}")
