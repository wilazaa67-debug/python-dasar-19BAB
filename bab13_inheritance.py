# Implementasi Inheritance (Pewarisan) di Python
class Pengguna:  # Parent Class (Superclass)
    def __init__(self, nama, sekolah):
        self.nama = nama
        self.sekolah = sekolah

    def info_dasar(self):
        print(f"Nama: {self.nama} | Sekolah: {self.sekolah}")

class Siswa(Pengguna):  # Child Class (Subclass) mewarisi class Pengguna
    def __init__(self, nama, sekolah, jurusan):
        super().__init__(nama, sekolah)  # Memanggil constructor parent class
        self.jurusan = jurusan

    def info_lengkap(self):
        self.info_dasar()
        print(f"Jurusan: {self.jurusan}")

# Membuat object dari child class Siswa
siswa_rpl = Siswa("Wiliandri", "SMKN 2 Subang", "Rekayasa Perangkat Lunak")
siswa_rpl.info_lengkap()