# Implementasi Dictionary (pasangan key-value) di Python
profil_siswa = {
    "nama": "Wiliandri",
    "kelas": "XI RPL",
    "sekolah": "SMKN 2 Subang",
    "nilai": 92
}

print("Data Dictionary Awal:", profil_siswa)
print("Nama Siswa:", profil_siswa["nama"])

# Mengubah nilai dan menambah key baru
profil_siswa["nilai"] = 96
profil_siswa["bahasa_favorit"] = "Python"

print("\nData Setelah Diperbarui:")
for key, value in profil_siswa.items():
    print(f"- {key}: {value}")