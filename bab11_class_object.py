# Implementasi Class & Object (OOP Dasar) di Python
class Siswa:
    # Constructor (__init__) untuk inisialisasi atribut
    def __init__(self, nama, kelas, jurusan):
        self.nama = nama
        self.kelas = kelas
        self.jurusan = jurusan

    # Method untuk menampilkan profil siswa
    def perkenalan(self):
        print(f"Halo, saya {self.nama} dari kelas {self.kelas} {self.jurusan}.")

# Membuat Object (instansiasi) dari class Siswa
siswa1 = Siswa("Wiliandri", "XI", "RPL")
siswa2 = Siswa("Budi Santoso", "XI", "RPL")

# Memanggil method pada masing-masing object
siswa1.perkenalan()
siswa2.perkenalan()