from paket_akademik import nilai

nilai_praktikum = [88, 92, 95, 90]
rata_rata = nilai.hitung_rata_rata(nilai_praktikum)
status = nilai.cek_kelulusan(rata_rata)
print('Daftar Nilai:', nilai_praktikum)
print('Rata-rata Nilai:', round(rata_rata, 2))
print('Status Kelulusan:', status)
