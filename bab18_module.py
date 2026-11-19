# Implementasi Module (Built-in Module & Custom Module) di Python
import math
import modul_matematika

# 1. Menggunakan built-in module bawaan Python (math)
akar_kuadrat = math.sqrt(64)
print("Akar kuadrat dari 64 (modul math):", akar_kuadrat)

# 2. Menggunakan custom module (modul_matematika)
hasil_tambah = modul_matematika.tambah(12, 8)
hasil_kali = modul_matematika.kali(6, 7)

print("Hasil Tambah (12 + 8):", hasil_tambah)
print("Hasil Kali (6 x 7):", hasil_kali)