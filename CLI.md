# 💻 Panduan Perintah CLI Ape Framework

Halaman ini berisi daftar perintah CLI Ape Framework penting yang digunakan untuk inisialisasi, kompilasi, manajemen akun, eksekusi skrip, dan pengujian dalam proyek ini.

---

## 🛠️ Inisialisasi & Kompilasi Proyek

* **Menginisialisasi Proyek Baru:**
  ```bash
  ape init
  ```
  *Fungsi: Menginisialisasi proyek baru dengan struktur direktori standar Ape (`contracts/`, `tests/`, `scripts/`, dll).*

* **Melakukan Kompilasi Solidity:**
  ```bash
  ape compile
  ```
  *Fungsi: Melakukan kompilasi seluruh smart contract Solidity yang berada di dalam folder `contracts/`.*

* **Melakukan Kompilasi Ulang (Clean Compile):**
  ```bash
  ape compile --force
  ```
  *Fungsi: Melakukan kompilasi ulang seluruh smart contract secara paksa (bersih), mengabaikan cache kompilasi sebelumnya.*

---

## 🔑 Manajemen Akun Wallet

Ape menyediakan modul bawaan untuk mengelola akun lokal terenkripsi secara aman.

* **Melihat Daftar Akun:**
  ```bash
  ape accounts list
  ```
  *Fungsi: Menampilkan seluruh akun wallet lokal yang tersimpan di dalam Ape.*

* **Mengimpor Akun Wallet Baru:**
  ```bash
  ape accounts import <wallet_name>
  ```
  *Fungsi: Mengimpor private key Anda ke dalam Ape dan menyimpannya dengan nama alias `<wallet_name>`.*

* **Menghapus Akun Wallet:**
  ```bash
  ape accounts delete <wallet_name>
  ```
  *Fungsi: Menghapus akun wallet lokal bernama `<wallet_name>` dari penyimpanan Ape.*

---

## 🏃 Eksekusi Skrip & Pengecekan Balance

* **Mengecek Saldo Akun:**
  ```bash
  ape run check_balance <wallet_name> --network ethereum:ganache_local
  ```
  *Fungsi: Menjalankan skrip `check_balance.py` untuk memeriksa saldo native coin milik `<wallet_name>` pada jaringan lokal Ganache.*

---

## 🧪 Pengujian / Unit Testing

* **Menjalankan Unit Test:**
  ```bash
  ape test -s
  ```
  *Fungsi: Menjalankan seluruh skrip pengujian (unit test) yang berada di dalam folder `tests/` dengan menampilkan output standar (`stdout` / logs).*
