# 📝 Smart Contract TodoList

Proyek ini berisi implementasi smart contract **TodoList** sederhana yang ditulis menggunakan bahasa pemrograman Solidity. Kontrak ini memungkinkan pengguna untuk membuat, membaca, memperbarui, dan menghapus daftar tugas (Task) secara terdesentralisasi.

Setiap tugas yang dibuat hanya dapat diakses, diubah, dan dihapus oleh pemilik (*owner*) yang membuat tugas tersebut.

---

## 🛠️ Fitur Kontrak Pintar

1. **Pembuatan Tugas (Create)**: Pengguna dapat menambahkan tugas baru dengan konten teks tertentu.
2. **Pembacaan Tugas (Read)**: Pemilik tugas dapat melihat informasi detail tugas berdasarkan ID tugas.
3. **Pembaruan Konten (Update)**: Pemilik tugas dapat memperbarui isi teks tugas yang telah dibuat.
4. **Penghapusan Tugas (Delete)**: Pemilik tugas dapat menghapus tugas yang sudah tidak diperlukan.

---

## 📖 Detail Struktur Data & State Variables

### 1. Struct `Task`
Struktur data untuk mendefinisikan sebuah tugas:
```solidity
struct Task {
    uint256 id;           // ID unik tugas
    address owner;        // Alamat wallet pembuat tugas
    string content;       // Konten/teks tugas
    bool isCompleted;     // Status penyelesaian tugas (default: false)
}
```

### 2. State Variables
* **`taskCount`**: Variabel publik bertipe `uint256` untuk menghitung total tugas yang pernah dibuat sekaligus menjadi ID untuk tugas berikutnya.
* **`tasks`**: Mapping dari ID tugas (`uint256`) ke struct `Task`.

---

## 🔒 Modifiers

Kontrak ini menggunakan modifier untuk menjaga keamanan data:
* **`taskExists(uint256 _id)`**: Memastikan bahwa tugas dengan ID tertentu ada (ID tidak sama dengan `0`). Jika tidak ada, transaksi dibatalkan dengan pesan `"task tidak di temukan"`.
* **`onlyTaskOwner(uint256 _id)`**: Memastikan bahwa hanya pembuat tugas (`msg.sender` sama dengan `owner`) yang dapat mengakses atau memodifikasi tugas tersebut. Jika bukan pemilik, transaksi dibatalkan dengan pesan `"anda bukan pemilik task ini"`.

---

## 💻 Fungsi-Fungsi Kontrak (Functions)

### 1. `createTask`
Digunakan untuk membuat tugas baru.
```solidity
function createTask(string calldata _content) public
```
* **Syarat**: Konten tugas (`_content`) tidak boleh kosong.
* **Proses**: Meningkatkan `taskCount`, lalu menyimpan data tugas baru ke mapping `tasks`.

### 2. `getTask`
Digunakan untuk mengambil/membaca informasi tugas.
```solidity
function getTask(uint256 _id) public view returns (uint256, string memory, bool)
```
* **Modifier**: `taskExists(_id)`, `onlyTaskOwner(_id)`.
* **Output**: Mengembalikan ID tugas, teks konten tugas, dan status penyelesaian (`isCompleted`).

### 3. `updateTaskContent`
Digunakan untuk mengedit isi teks dari tugas.
```solidity
function updateTaskContent(uint256 _id, string calldata _newContent) public
```
* **Modifier**: `taskExists(_id)`, `onlyTaskOwner(_id)`.
* **Syarat**: Konten baru (`_newContent`) tidak boleh kosong.

### 4. `deleteTasks`
Digunakan untuk menghapus tugas berdasarkan ID.
```solidity
function deleteTasks(uint256 _id) public
```
* **Modifier**: `taskExists(_id)`, `onlyTaskOwner(_id)`.
* **Proses**: Menghapus entry tugas dari mapping menggunakan keyword bawaan solidity `delete`.

---

## 🚀 Cara Penggunaan / Deployment

Kontrak pintar ini menggunakan Solidity versi compiler `^0.8.20`. Anda dapat mengompilasi dan mendeploy kontrak ini menggunakan tools seperti:
1. **Remix IDE** (remix.ethereum.org)
2. **Hardhat** atau **Foundry**
3. **Ape Framework**
