# PDF_METADATA
🚀 PDF Metadata Extractor
Sebuah script Python sederhana untuk mengekstrak metadata lengkap dari semua file PDF dalam sebuah folder. Output ditampilkan di terminal dengan format yang detail dan rapi, terinspirasi dari exiftool, untuk memberikan wawasan mendalam tentang setiap file.

✨ Fitur Utama
Ekstraksi Komprehensif: Mengambil metadata dari sistem file (ukuran, tanggal modifikasi, dll.) dan dari internal PDF (Judul, Penulis, Jumlah Halaman, dll.).

Analisis Batch: Secara otomatis menganalisis semua file .pdf yang ada di dalam folder yang Anda tentukan.

Output Terstruktur: Menampilkan metadata di terminal dengan format yang jelas dan terkategori untuk setiap file.

Kompatibilitas: Didesain agar kompatibel dengan berbagai versi library PyPDF2.

⚙️ Prasyarat
Sebelum memulai, pastikan Anda sudah menginstal:

Python (versi 3.6 atau yang lebih baru)

pip (biasanya sudah terinstal bersama Python)

🛠️ Instalasi
Ikuti langkah-langkah berikut untuk menyiapkan dan menjalankan script.

Clone Repositori
Buka terminal atau Git Bash, lalu clone repositori ini ke komputer Anda:

Bash

git clone https://github.com/nama-anda/nama-repositori-anda.git
(Ganti nama-anda dan nama-repositori-anda)

Atau, cukup unduh file pdf_meta_final.py dari halaman ini.

Masuk ke Direktori Proyek

Bash

cd nama-repositori-anda
Instal Library yang Dibutuhkan
Script ini hanya membutuhkan satu library eksternal, yaitu PyPDF2. Instal dengan perintah:

Bash

pip install PyPDF2
▶️ Cara Menjalankan Script
Siapkan Folder PDF Anda
Buat sebuah folder di dalam direktori proyek (atau di mana saja) dan letakkan semua file PDF yang ingin Anda analisis di dalamnya. Misalnya, Anda membuat folder bernama folder_saya.

/proyek-anda/
├── pdf_meta_final.py    <-- Script utama
└── /folder_saya/        <-- Folder berisi PDF
    ├── laporan_mingguan.pdf
    ├── jurnal_penelitian.pdf
    └── dokumen_penting.pdf
Jalankan Perintah di Terminal
Buka terminal dari direktori proyek Anda dan jalankan script dengan memberikan path ke folder PDF Anda sebagai argumen.

Format Perintah:

Bash

python pdf_meta_final.py <path_ke_folder>
Contoh Praktis:

Bash

python pdf_meta_final.py ./folder_saya
📋 Contoh Output di Terminal
Setelah script dijalankan, Anda akan melihat output yang detail untuk setiap file PDF, seperti di bawah ini:

Bash

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

... (output serupa untuk file lainnya) ...

--- ✨ Analisis Selesai. Total 3 file PDF diproses. ---
