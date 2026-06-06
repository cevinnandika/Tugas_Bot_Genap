# Auto-Solver Bot: Nikko Puzzle (Genap) 🤖🔢

Repository ini berisi program bot otomatis (*auto-solver*) berbasis Python yang dirancang khusus untuk menyelesaikan tantangan matematika interaktif pada program biner `nikko_puzzle_windows_amd64.exe`. Program ini mengintegrasikan manipulasi *I/O Stream* secara dinamis dan pemrosesan teks *real-time* untuk melewati proteksi *timeout* ketat dari sistem.

---

## 🚀 Fitur Utama & Arsitektur

* **Non-Blocking Character Stream Reader:** Menggunakan pembacaan karakter-per-karakter (`process.stdout.read(1)`) alih-alih pembacaan baris (`readline`). Pendekatan ini krusial untuk mencegah bot *stuck* (gantung) pada prompt input CLI yang tidak diakhiri karakter *newline* (`\n`).
* **State-Machine Input Flow:** Alur otomasi pendaftaran data diri dikendalikan oleh *boolean flags* (`menu_terpilih`, `nama_terkirim`, `nim_terkirim`). Struktur ini menjamin data dikirim berurutan dan mencegah kegagalan *pipe* akibat penulisan data yang terlalu cepat atau bertabrakan.
* **Adaptive Geometry Solver:** Menggunakan *Regular Expression* (Regex) adaptif yang mampu mendeteksi nama bangun datar sekaligus menentukan rumus kalkulasi yang tepat berdasarkan jenis operasi (**Luas** atau **Keliling**) secara *on-the-fly*.
* **Sub-1-Second Response Rate:** Komputasi lokal dan pengiriman jawaban diselesaikan di bawah 0.1 detik, memastikan bot lolos dari batasan waktu *timeout* (1 detik) yang diatur oleh sistem tantangan.
* **Unicode Character Bypass:** Menggunakan konfigurasi `errors='ignore'` pada encoding pipa `utf-8` untuk menangani interferensi karakter sampah (*garbage characters*) seperti simbol kuadrat (`cmÂ²`) yang dapat merusak pola regex.

---

## 🛠️ Matriks Cakupan Rumus Matematika

Bot ini telah diuji dan berhasil menyelesaikan 100 soal berturut-turut tanpa gagal dengan cakupan rumus sebagai berikut:

| Bangun Datar | Operasi Luas | Operasi Keliling |
| :--- | :--- | :--- |
| **Persegi** | $s \times s$ | $4 \times s$ |
| **Persegi Panjang** | $p \times l$ | $2 \times (p + l)$ |
| **Segitiga** | $\frac{a \times t}{2}$ | Penjumlahan seluruh sisi |
| **Lingkaran** | $\frac{22 \times r \times r}{7}$ | $\frac{2 \times 22 \times r}{7}$ |

---

## 📁 Struktur Direktori

```text
Tugas_Bot_Genap/
│
├── nikko_puzzle_windows_amd64/
│   └── nikko_puzzle_windows_amd64.exe  # Program biner target (Tantangan)
│
├── bot_MTK.py                         # Source code utama bot otomasi
└── README.md                          # Dokumentasi proyek

💻 Cara Penggunaan
Pastikan lingkungan perangkat Anda telah terinstal Python 3.x.

Buka terminal atau Command Prompt, lalu masuk ke direktori root proyek ini:

Bash
cd Tugas_Bot_Genap
Eksekusi program bot dengan perintah:

Bash
python bot_MTK.py
