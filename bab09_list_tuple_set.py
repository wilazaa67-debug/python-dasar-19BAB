# Implementasi List, Tuple, dan Set di Python

# 1. List (berurutan, dapat diubah/mutable, boleh duplikat)
bahasa_pemrograman = ["Python", "JavaScript", "PHP"]
bahasa_pemrograman.append("Golang")
print("List:", bahasa_pemrograman)
print("Elemen pertama List:", bahasa_pemrograman[0])

# 2. Tuple (berurutan, tidak dapat diubah/immutable)
koordinat_sekolah = (-6.5644, 107.7606)
print("\nTuple:", koordinat_sekolah)
print("Latitude:", koordinat_sekolah[0])

# 3. Set (tidak berurutan, otomatis menghapus data duplikat)
angka_unik = {10, 20, 20, 30, 40, 40}
angka_unik.add(50)
print("\nSet (tanpa duplikat):", angka_unik)