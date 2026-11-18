# Implementasi Encapsulation (Enkapsulasi) di Python
class AkunSiswa:
    def __init__(self, nama, nilai):
        self.nama = nama          # Atribut public
        self.__nilai = nilai      # Atribut private (diawali dua garis bawah __)

    # Getter untuk membaca atribut private
    def get_nilai(self):
        return self.__nilai

    # Setter untuk mengubah atribut private dengan validasi
    def set_nilai(self, nilai_baru):
        if 0 <= nilai_baru <= 100:
            self.__nilai = nilai_baru
        else:
            print("Error: Nilai harus berada di rentang 0 sampai 100!")

akun = AkunSiswa("Wiliandri", 85)
print("Nama Siswa:", akun.nama)
print("Nilai Awal:", akun.get_nilai())

# Mengubah nilai melalui method setter
akun.set_nilai(95)
print("Nilai Setelah Diperbarui:", akun.get_nilai())