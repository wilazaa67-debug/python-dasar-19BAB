# Implementasi Function (Fungsi) di Python

# 1. Fungsi sederhana tanpa parameter
def sapa_praktikan():
    print("Halo! Selamat datang di Praktikum Python Dasar.")

# 2. Fungsi dengan parameter dan default value
def perkenalan(nama, kelas="XI RPL"):
    print(f"Nama: {nama} | Kelas: {kelas}")

# 3. Fungsi dengan nilai kembalian (return)
def hitung_luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    return luas

# Memanggil fungsi
sapa_praktikan()
perkenalan("Wiliandri")
hasil_luas = hitung_luas_persegi_panjang(10, 5)
print(f"Luas Persegi Panjang (10 x 5): {hasil_luas}")