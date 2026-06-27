# 🎮 Proyek TebakAngka - Panduan Menjalankan Proyek

Panduan ini berisi langkah-langkah berurutan untuk menjalankan proyek game Web3 **TebakAngka** menggunakan **Ape Framework**, mulai dari persiapan lingkungan, kompilasi, deployment, hingga bermain game.

---

## 🎥 Video Panduan / Tutorial
Untuk memudahkan proses instalasi dan konfigurasi, silakan tonton video tutorial berikut:
1. [🌐 Tutorial Instalasi MetaMask](https://studentgunadarmaacid-my.sharepoint.com/:v:/g/personal/andana_student_gunadarma_ac_id/IQDDAFOi8_RfRqDODY9EKIWUAZBrgB0nsnOIlV74B8-0oZQ?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=No32sf)
2. [🚰 Tutorial Tambah Network Testnet & Claim Faucet](https://studentgunadarmaacid-my.sharepoint.com/:v:/g/personal/andana_student_gunadarma_ac_id/IQAefxj-SnOiRJj3bk2ZZhWTAeDCavtjB0fNOMi_qh18i7w?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=WlZh7m)
3. [🔑 Tutorial Mendapatkan API Key Pinata](https://studentgunadarmaacid-my.sharepoint.com/:v:/g/personal/andana_student_gunadarma_ac_id/IQAVr-e7THg_RKrhf4cMdNc9AfXqaxOxZTdcn66bRNs1L4k?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=pJLstT)
4. [🔍 Tutorial Mendapatkan API Key Etherscan](https://studentgunadarmaacid-my.sharepoint.com/:v:/g/personal/andana_student_gunadarma_ac_id/IQAlkk7V_CWURIihrQ1sIjFgAcptDgj4bD_RHQtKiG3ktfQ?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=fyiUfI)

---

## 🛠️ Langkah 1: Persiapan & Setup Lingkungan

### 1. Buat & Aktifkan Virtual Environment Python
Karena folder `env/` dikecualikan dari Git (masuk `.gitignore`), Anda perlu membuat virtual environment baru dan menginstal dependensi saat pertama kali setup:

```bash
# Buat virtual environment
python3 -m venv env

# Aktifkan virtual environment
source env/bin/activate

# Instal dependensi Python & plugin Ape
pip install -r requirements.txt
```


### 2. Duplikasi & Konfigurasi `.env`
Salin file `.env.example` ke `.env`:
```bash
cp .env.example .env
```
Buka file `.env` dan masukkan API Key yang valid:
* **`ETHERSCAN_API_KEY`**: Digunakan untuk verifikasi contract otomatis di Etherscan.
  > 🎬 *Panduan mencari API Key Etherscan dapat dilihat pada [Video Tutorial Etherscan](https://studentgunadarmaacid-my.sharepoint.com/:v:/g/personal/andana_student_gunadarma_ac_id/IQAlkk7V_CWURIihrQ1sIjFgAcptDgj4bD_RHQtKiG3ktfQ?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=fyiUfI).*
* **`VITE_PINATA_API_KEY`** & **`VITE_PINATA_SECRET_API_KEY`**: Digunakan untuk mengunggah metadata dan gambar NFT secara otomatis ke IPFS via Pinata.
  > 🎬 *Panduan mencari API Key Pinata dapat dilihat pada [Video Tutorial Pinata](https://studentgunadarmaacid-my.sharepoint.com/:v:/g/personal/andana_student_gunadarma_ac_id/IQAVr-e7THg_RKrhf4cMdNc9AfXqaxOxZTdcn66bRNs1L4k?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=pJLstT).*

### 3. Persiapkan Akun Wallet Ape
Impor akun wallet (Sepolia atau Testnet lokal) yang akan digunakan sebagai Deployer dan Pemain:
```bash
ape accounts import <nama_akun_anda>
```
*Ape akan meminta Anda memasukkan Private Key dan membuat password pengaman untuk akun tersebut.*
  > 🎬 *Jika Anda belum memiliki wallet, lihat [Video Tutorial MetaMask](https://studentgunadarmaacid-my.sharepoint.com/:v:/g/personal/andana_student_gunadarma_ac_id/IQDDAFOi8_RfRqDODY9EKIWUAZBrgB0nsnOIlV74B8-0oZQ?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=No32sf).*

---

## ⚙️ Langkah 2: Kompilasi Smart Contract

Lakukan kompilasi smart contract Solidity (`contracts/`) untuk menghasilkan ABI dan bytecode yang diperlukan:
```bash
ape compile
```
Jika Anda melakukan perubahan struktural pada contract dan ingin memaksa kompilasi ulang dari awal, gunakan flag `--force`:
```bash
ape compile --force
```

---

## 🚀 Langkah 3: Mendeploy Smart Contract (Deploy)

Gunakan perintah `deploy` untuk mendeploy token ERC20 (`TebakAngkaCoin`), NFT ERC721 (`TebakAngkaNFT`), dan contract game utama (`TebakAngka`) ke jaringan pilihan Anda.

### Contoh Deploy ke Jaringan Testnet Sepolia:
```bash
ape run deploy <nama_akun_anda> --network ethereum:sepolia:node
```
  > 🎬 *Panduan menambahkan network Sepolia dan melakukan claim faucet ETH gratis dapat dilihat pada [Video Tutorial Network & Faucet](https://studentgunadarmaacid-my.sharepoint.com/:v:/g/personal/andana_student_gunadarma_ac_id/IQAefxj-SnOiRJj3bk2ZZhWTAeDCavtjB0fNOMi_qh18i7w?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=WlZh7m).*

> 💡 **Info**: Setelah deploy berhasil, script secara otomatis akan menulis dan mengupdate alamat contract baru Anda ke dalam file `.env` pada variabel:
> * `TEBAK_ANGKA_COIN_ADDRESS`
> * `TEBAK_ANGKA_NFT_ADDRESS`
> * `TEBAK_ANGKA_ADDRESS`

---

## 🎲 Langkah 4: Memulai Permainan (Play)

Setelah alamat game terupdate di `.env` (atau menggunakan argumen `--address`), Anda dapat menebak angka antara **1 sampai 5**.

### Contoh Menjalankan Game Tebak Angka 3 di Sepolia:
```bash
ape run play <nama_akun_anda> 3 --network ethereum:sepolia:node
```

### Cara Kerja Script Play:
1. **Mengunggah Gambar & Metadata ke IPFS**: Script akan membaca gambar di folder `images/win.png` dan `images/lose.png`, mengunggahnya ke Pinata, lalu membuat metadata URI JSON untuk NFT pemenang/kalah.
2. **Kirim Transaksi**: Mengirim transaksi tebakan ke contract `TebakAngka.guess()`.
3. **Membaca Hasil**: Membaca event/log `GuessMode` dari blockchain untuk menentukan kemenangan. Jika tebakan Anda benar, Anda akan mendapat token `TAC` dan NFT pemenang ter-mint ke wallet Anda!

---

## 📖 Referensi Lainnya
* Untuk daftar perintah lengkap terkait manajemen akun dan command framework Ape lainnya, silakan lihat [Panduan CLI Ape](file:///home/adit/Documents/coding/project-workshop/gunadarma-io/week-2/CLI.md).
