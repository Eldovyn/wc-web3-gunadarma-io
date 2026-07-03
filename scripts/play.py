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
@click.option("--address", default=None, help="Alamat (Address) dari kontrak RNG Showcase yang sudah dideploy")
@click.option("--network", default="ethereum:sepolia:node", help="Network specifier")
def cli(account_name, guess_number, address, network):
    if not (1 <= guess_number <= 5):
        print("Error: Parameter input harus antara 1 sampai 5!")
        return

    if not address:
        address = os.getenv("RNG_SHOWCASE_ADDRESS")
        if not address or not address.startswith("0x") or len(address) != 42:
            print("Error: Contract address must be provided via --address or set as a valid RNG_SHOWCASE_ADDRESS in .env!")
            return

    with networks.parse_network_choice(network) as provider:
        print(f"Active Network: {provider.network.name}")
        
        try:
            player = accounts.load(account_name)
            player.set_autosign(True)
        except KeyError:
            print(f"Error: Account '{account_name}' is not found in Ape.")
            return

        print(f"Mengeksekusi interaksi on-chain menggunakan akun: {player.address}")
        
        game = project.TebakAngka.at(address)
        nft_contract = project.TebakAngkaNFT.at(game.nftContract())
        
        print(f"Mengirim parameter input {guess_number} ke kontrak {game.address}...")
        
        try:
            print("Mengunggah gambar dan metadata ke Pinata...")
            win_image_path = "images/win.png"
            lose_image_path = "images/lose.png"
            
            win_image_hash = upload_file_to_pinata(win_image_path, "RNG_Showcase_Success_Image")
            lose_image_hash = upload_file_to_pinata(lose_image_path, "RNG_Showcase_Fail_Image")
            
            win_metadata = {
                "name": "Reward NFT (Success)",
                "description": f"NFT insentif eksekusi RNG Showcase. Validasi kondisi terpenuhi dengan parameter input {guess_number}.",
                "image": f"https://gateway.pinata.cloud/ipfs/{win_image_hash}",
                "attributes": [
                    {"trait_type": "Input", "value": guess_number},
                    {"trait_type": "Validasi", "value": "Berhasil"},
                    {"trait_type": "Konteks", "value": "RNG Showcase"}
                ]
            }
            
            lose_metadata = {
                "name": "Participation NFT (Fail)",
                "description": f"NFT partisipasi eksekusi RNG Showcase. Validasi kondisi gagal dengan parameter input {guess_number}.",
                "image": f"https://gateway.pinata.cloud/ipfs/{lose_image_hash}",
                "attributes": [
                    {"trait_type": "Input", "value": guess_number},
                    {"trait_type": "Validasi", "value": "Gagal"},
                    {"trait_type": "Konteks", "value": "RNG Showcase"}
                ]
            }
            
            win_metadata_hash = upload_json_to_pinata(win_metadata, f"RNG_Showcase_Success_{int(time.time())}.json")
            lose_metadata_hash = upload_json_to_pinata(lose_metadata, f"RNG_Showcase_Fail_{int(time.time())}.json")
            
            win_uri = f"https://gateway.pinata.cloud/ipfs/{win_metadata_hash}"
            lose_uri = f"https://gateway.pinata.cloud/ipfs/{lose_metadata_hash}"
            print(f"Metadata berhasil diunggah! Win URI: {win_uri}")

            tx = game.guess(guess_number, win_uri, lose_uri, sender=player, gas_limit=800000)
            print(f"\nTransaksi berhasil! Hash: {tx.txn_hash}")
            
            logs = list(tx.decode_logs(game.GuessMode))
            if logs:
                event = logs[0]
                print("\n--- HASIL INTERAKSI ON-CHAIN ---")
                print(f"Input Anda: {event.guess}")
                print(f"Hasil RNG: {event.correctNumber}")
                
                if event.won:
                    print("🎉 VALIDASI BERHASIL! Kondisi parameter terpenuhi.")
                    print("🎁 Smart contract mengeksekusi automated distribution: 10 Reward Token dan 1 Reward NFT.")
                else:
                    print("😢 VALIDASI GAGAL! Input tidak sesuai dengan hasil RNG.")
                
                transfer_logs = list(tx.decode_logs(nft_contract.Transfer))
                if transfer_logs:
                    for log in transfer_logs:
                        if log.to == player.address:
                            print(f"🎨 NFT Minted! Contract: {nft_contract.address} | Token ID: {log.tokenId}")
                            break
                print("------------------")
            else:
                print("Event GuessMode tidak ditemukan di transaksi ini.")
                
        except Exception as e:
            print(f"Error saat mengeksekusi transaksi: {e}")
