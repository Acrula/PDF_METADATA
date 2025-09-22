import sys
import os
import stat
from datetime import datetime
from PyPDF2 import PdfReader
import xml.etree.ElementTree as ET

def format_size(size_bytes):
    """Mengubah ukuran byte menjadi format KB yang mudah dibaca."""
    if size_bytes == 0:
        return "0 B"
    s = size_bytes / 1024
    return f"{s:.2f} KB"

def format_timestamp(ts):
    """Mengubah timestamp menjadi format tanggal dan waktu yang mudah dibaca."""
    return datetime.fromtimestamp(ts).strftime('%Y:%m:%d %H:%M:%S')

def parse_xmp_metadata(pdf_reader):
    """Mengekstrak metadata detail dari blok data XMP jika ada."""
    xmp_data = {}
    try:
        xmp = pdf_reader.xmp_metadata
        if xmp:
            ns = {
                'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
                'dc': 'http://purl.org/dc/elements/1.1/',
                'xmp': 'http://ns.adobe.com/xap/1.0/',
                'xmpMM': 'http://ns.adobe.com/xap/1.0/mm/',
                'pdf': 'http://ns.adobe.com/pdf/1.3/',
            }
            root = ET.fromstring(xmp.custom_properties)
            desc = root.find('rdf:Description', ns)
            if desc is not None:
                xmp_data['XMP Toolkit'] = desc.get('{http://ns.adobe.com/xap/1.0/}xmptk', 'N/A')
                xmp_data['Creator Tool'] = desc.findtext('xmp:CreatorTool', None, ns)
                xmp_data['Document ID'] = desc.findtext('xmpMM:DocumentID', None, ns)
                xmp_data['Instance ID'] = desc.findtext('xmpMM:InstanceID', None, ns)
    except Exception:
        pass
    return xmp_data

def display_pdf_metadata(file_path):
    """Mengekstrak dan menampilkan metadata lengkap dari SATU file PDF."""
    try:
        file_stat = os.stat(file_path)
        permissions = stat.filemode(file_stat.st_mode)

        reader = PdfReader(file_path)
        meta = reader.metadata
        xmp_meta = parse_xmp_metadata(reader)

        metadata = {
            "File Name": os.path.basename(file_path),
            "Directory": os.path.dirname(file_path) or ".",
            "File Size": format_size(file_stat.st_size),
            "File Modification Date/Time": format_timestamp(file_stat.st_mtime),
            "File Access Date/Time": format_timestamp(file_stat.st_atime),
            "File Inode Change Date/Time": format_timestamp(file_stat.st_ctime),
            "File Permissions": permissions,
            "File Type": "PDF", "File Type Extension": "pdf", "MIME Type": "application/pdf",
            "PDF Version": reader.pdf_header.replace('%PDF-', ''),
            "Linearized": "Yes" if hasattr(reader, 'is_linearized') and reader.is_linearized else "No",
            "Page Count": len(reader.pages),
            "Language": meta.get('/Lang', 'N/A'),
            "Tagged PDF": "Yes" if hasattr(reader, 'is_tagged') and reader.is_tagged else "No",
            "XMP Toolkit": xmp_meta.get('XMP Toolkit', 'N/A'),
            "Producer": meta.producer or "N/A",
            "Creator": meta.creator or "N/A",
            "Creator Tool": xmp_meta.get('Creator Tool') or meta.creator or "N/A",
            "Create Date": meta.creation_date.strftime('%Y:%m:%d %H:%M:%S') if meta.creation_date else "N/A",
            "Modify Date": meta.modification_date.strftime('%Y:%m:%d %H:%M:%S') if meta.modification_date else "N/A",
            "Document ID": xmp_meta.get('Document ID', 'N/A'),
            "Instance ID": xmp_meta.get('Instance ID', 'N/A'),
            "Author": meta.author or "N/A",
        }
        
        # Menampilkan output dengan rapi
        print(f"\n{'='*25} METADATA UNTUK: {os.path.basename(file_path)} {'='*25}")
        for key, value in metadata.items():
            print(f"{key:<30}: {value}")
        print(f"{'='* (68 + len(os.path.basename(file_path)))}")

    except Exception as e:
        print(f"\n{'!'*25} GAGAL MEMPROSES: {os.path.basename(file_path)} {'!'*25}")
        print(f"Error: {e}")

def analyze_folder(folder_path):
    """Menganalisis semua file PDF dalam folder yang diberikan."""
    if not os.path.isdir(folder_path):
        print(f"Error: Folder '{folder_path}' tidak ditemukan atau bukan sebuah direktori.")
        return

    print(f"--- 🚀 Memulai Analisis Metadata untuk Folder: {folder_path} ---")
    
    found_pdfs = 0
    for filename in sorted(os.listdir(folder_path)): # Mengurutkan file berdasarkan nama
        if filename.lower().endswith('.pdf'):
            found_pdfs += 1
            full_path = os.path.join(folder_path, filename)
            display_pdf_metadata(full_path) # Memanggil fungsi analisis untuk setiap file
    
    if found_pdfs == 0:
        print("\n--- ⚠️ Tidak ada file PDF yang ditemukan di dalam folder tersebut. ---")
    else:
        print(f"\n--- ✨ Analisis Selesai. Total {found_pdfs} file PDF diproses. ---")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("\nPenggunaan: python pdf_meta_final.py <path_ke_folder>")
        print("Contoh: python pdf_meta_final.py ./folderpdf")
        sys.exit(1)

    target_folder = sys.argv[1]
    analyze_folder(target_folder)