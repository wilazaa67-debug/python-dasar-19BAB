# Implementasi Exception Handling (Penanganan Eksepsi) di Python
def bagi_angka(a, b):
    try:
        hasil = a / b
    except ZeroDivisionError:
        print("Error: Tidak dapat membagi bilangan dengan nol (0)!")
    except TypeError:
        print("Error: Input harus berupa angka!")
    else:
        print(f"Hasil pembagian {a} / {b} = {hasil}")
    finally:
        print("Proses pengecekan selesai.\n")

# 1. Uji coba pembagian normal
bagi_angka(20, 4)

# 2. Uji coba pembagian dengan nol (memicu ZeroDivisionError)
bagi_angka(10, 0)