# Implementasi File Handling (Write, Append, dan Read File) di Python
nama_file = "catatan_praktikum.txt"

# 1. Menulis file baru (mode 'w' / write)
with open(nama_file, "w", encoding="utf-8") as file:
    file.write("Praktikum Python Dasar - Santrikoding\n")
    file.write("Bab #17: File Handling berhasil dijalankan.\n")

# 2. Menambahkan baris teks ke file (mode 'a' / append)
with open(nama_file, "a", encoding="utf-8") as file:
    file.write("Status: Selesai diuji oleh Wiliandri.\n")

# 3. Membaca seluruh isi file (mode 'r' / read)
print("=== Isi Berkas catatan_praktikum.txt ===")
with open(nama_file, "r", encoding="utf-8") as file:
    isi = file.read()
    print(isi)