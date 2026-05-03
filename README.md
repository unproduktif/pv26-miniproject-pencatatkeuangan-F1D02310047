# 💰 Smart Finance Tracker

Smart Finance Tracker merupakan aplikasi desktop berbasis Python dan PySide6 yang digunakan untuk mencatat dan mengelola transaksi keuangan pribadi seperti pemasukan dan pengeluaran. 

Aplikasi ini memungkinkan pengguna untuk:
- menambahkan transaksi
- mengedit transaksi
- menghapus transaksi
- mencari transaksi
- memfilter transaksi
- melihat ringkasan saldo secara real-time

Data transaksi disimpan menggunakan database SQLite sehingga data dapat tersimpan secara lokal pada perangkat pengguna.

---

# ✨ Fitur Utama

- ✅ Tambah transaksi keuangan
- ✅ Edit transaksi
- ✅ Hapus transaksi
- ✅ Dashboard ringkasan saldo
- ✅ Search transaksi
- ✅ Filter transaksi
- ✅ Penyimpanan data menggunakan SQLite
- ✅ Tampilan modern menggunakan QSS
- ✅ Struktur project menggunakan konsep Separation of Concerns (SoC)

---

# 🛠 Teknologi yang Digunakan

| Teknologi | Fungsi |
|---|---|
| Python | Bahasa pemrograman utama |
| PySide6 | Framework GUI desktop |
| SQLite | Database lokal |
| QSS | Styling antarmuka aplikasi |

---

# 📁 Struktur Project

```text
pv26-miniproject-pencatatkeuangan-F1D02310047/
│
├── main.py
│
├── database/
│   └── db_manager.py
│
├── ui/
│   ├── main_window.py
│   ├── transaction_dialog.py
│   └── about_dialog.py
│
├── styles/
│   └── style.qss
│
└── data/
    └── finance.db
```

---

# ▶ Cara Menjalankan Aplikasi

## 1. Clone Repository

```bash
git clone [https://github.com/username/repository.git](https://github.com/unproduktif/pv26-miniproject-pencatatkeuangan-F1D02310047.git)
```

---

## 2. Masuk ke Folder Project

```bash
cd pv26-miniproject-pencatatkeuangan-F1D02310047
```

---

## 3. Install Dependency

```bash
pip install PySide6
```

atau:

```bash
pip install -r requirements.txt
```

---

## 4. Jalankan Aplikasi

```bash
python main.py
```

---

# 👨‍💻 Author

**Dodi Wijaya**  
NIM: F1D02310047
