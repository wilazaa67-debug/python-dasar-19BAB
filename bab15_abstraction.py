from abc import ABC, abstractmethod

# Implementasi Abstraction (Abstraksi) di Python
class BangunDatar(ABC):
    @abstractmethod
    def hitung_luas(self):
        pass

    @abstractmethod
    def hitung_keliling(self):
        pass

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_luas(self):
        return self.sisi * self.sisi

    def hitung_keliling(self):
        return 4 * self.sisi

# Membuat object dari class turunan Persegi
persegi = Persegi(6)
print(f"Luas Persegi (sisi=6): {persegi.hitung_luas()}")
print(f"Keliling Persegi (sisi=6): {persegi.hitung_keliling()}")