# Implementasi Control Flow (Percabangan & Perulangan) di Python

# 1. Percabangan (if - elif - else)
nilai = 88
if nilai >= 90:
    predikat = "A (Sangat Baik)"
elif nilai >= 80:
    predikat = "B (Baik)"
else:
    predikat = "C (Cukup)"

print(f"Nilai: {nilai} -> Predikat: {predikat}")

# 2. Perulangan for
print("\nPerulangan for (1 sampai 5):")
for i in range(1, 6):
    print(f"Iterasi ke-{i}")

# 3. Perulangan while
print("\nPerulangan while (hitung mundur):")
hitungan = 3
while hitungan > 0:
    print("Hitung mundur:", hitungan)
    hitungan -= 1