# 🚀 PDF Metadata Extractor

Sebuah script Python untuk mengekstrak metadata lengkap dari file-file PDF dalam sebuah folder. Output ditampilkan di terminal dengan format yang detail dan rapi, terinspirasi dari `exiftool`, untuk memberikan wawasan mendalam tentang setiap file.

---

## ✨ Fitur Utama

-   **Ekstraksi Komprehensif**: Mengambil metadata dari sistem file (ukuran, tanggal modifikasi) dan internal PDF (Judul, Penulis, Jumlah Halaman).
-   **Analisis Batch**: Menganalisis semua file `.pdf` secara otomatis di dalam folder yang ditentukan.
-   **Output Terstruktur**: Menampilkan metadata di terminal dengan format yang jelas untuk setiap file.
-   **Kompatibilitas**: Didesain agar kompatibel dengan berbagai versi library `PyPDF2`.

---

## ⚙️ Prasyarat

Sebelum memulai, pastikan Anda sudah memiliki:
-   Python (versi 3.6 atau yang lebih baru)
-   `pip` (Python package installer)

---

## 🛠️ Instalasi

Ikuti langkah-langkah berikut untuk menyiapkan script.

1. Clone Repositori
Buka terminal Anda, lalu clone repositori ini ke komputer.
```bash
git clone [https://github.com/nama-anda/nama-repositori-anda.git](https://github.com/nama-anda/nama-repositori-anda.git)
(Ganti nama-anda dan nama-repositori-anda dengan URL repositori Anda)

Atau, cukup unduh file pdf_meta_final.py dari halaman ini.

2. Masuk ke Direktori Proyek
cd nama-repositori-anda

3. Instal Library yang Dibutuhkan
Script ini membutuhkan library PyPDF2. Instal dengan perintah:

pip install PyPDF2

###▶️ Cara Menjalankan Script
Siapkan Folder PDF
Buat sebuah folder dan letakkan semua file PDF yang ingin dianalisis di dalamnya. Contoh struktur folder:

/proyek-anda/
├── pdf_meta_final.py    <-- Script utama
└── /folderpdf/        <-- Folder berisi PDF
    ├── laporan_mingguan.pdf
    ├── jurnal_penelitian.pdf
    └── dokumen_penting.pdf
Jalankan Perintah di Terminal
Buka terminal dari direktori proyek dan jalankan script, arahkan ke folder PDF Anda.

Format Perintah:

python pdf_meta_final.py <path_ke_folder>

Contoh Praktis:
python pdf_meta_final.py ./folderpdf
📋 Contoh Output di Terminal
Setelah script dijalankan, Anda akan melihat output detail untuk setiap file PDF, seperti di bawah ini:


--- 🚀 Memulai Analisis Metadata untuk Folder: ./folder_saya ---

========================= METADATA UNTUK: jurnal_penelitian.pdf =========================
File Name                     : jurnal_penelitian.pdf
Directory                     : ./folder_saya
File Size                     : 512.45 KB
File Modification Date/Time   : 2025:09:22 10:40:15
File Access Date/Time         : 2025:09:22 11:05:30
File Inode Change Date/Time   : 2025:09:22 10:40:11
File Permissions              : -rw-r--r--
File Type                     : PDF
File Type Extension           : pdf
MIME Type                     : application/pdf
PDF Version                   : 1.7
Linearized                    : No
Page Count                    : 15
Language                      : N/A
Tagged PDF                    : No
XMP Toolkit                   : N/A
Producer                      : Microsoft® Print to PDF
Creator                       : Microsoft® Word 365
Creator Tool                  : Microsoft® Word 365
Create Date                   : 2025:09:20 14:30:00
Modify Date                   : 2025:09:21 09:15:22
Document ID                   : N/A
Instance ID                   : N/A
Author                        : Dr. Budi Santoso
=======================================================================================




        ... (output serupa untuk fileai lnnya) ...

--- ✨ Analisis Selesai. Total 3 file PDF diproses. ---
