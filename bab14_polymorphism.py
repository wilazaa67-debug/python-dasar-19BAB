# Implementasi Polymorphism (Polimorfisme) di Python
class BahasaPemrograman:
    def deskripsi(self):
        print("Ini adalah bahasa pemrograman.")

class Python(BahasaPemrograman):
    def deskripsi(self):
        print("Python: Cocok untuk AI, Data Science, dan Backend Web.")

class JavaScript(BahasaPemrograman):
    def deskripsi(self):
        print("JavaScript: Bahasa utama untuk pengembangan Web Interaktif.")

class Golang(BahasaPemrograman):
    def deskripsi(self):
        print("Golang: Cepat dan efisien untuk sistem Backend dan Cloud.")

# Demonstrasi Polymorphism (nama method sama, perilaku berbeda tiap objek)
daftar_bahasa = [Python(), JavaScript(), Golang()]

for bahasa in daftar_bahasa:
    bahasa.deskripsi()