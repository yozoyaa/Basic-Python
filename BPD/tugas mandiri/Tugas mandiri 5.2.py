x = int(input("Masukkan bilangan bulat x: "))

try:
    hasil = 2*x**3 + 2*x + 15/x
    print("Hasil dari fungsi f(x) = 2x^3 + 2x + 15/x adalah:", hasil)
except ZeroDivisionError:
    print("Error: Pembagian dengan nol tidak diperbolehkan.")