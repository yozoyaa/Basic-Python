import math

def angka(pesan):
    while True:
        try:
            return float(input(pesan))
        except ValueError:
            print("Input yang dimasukan salah! Masukan Angka")


def luas_persegi(panjang, lebar):
    return float(panjang * lebar)


def luas_segitiga(alas, tinggi):
    return float(0.5 * (alas * tinggi))



def luas_lingkaran(radius):
    return float(math.pi * radius ** 2)


panjang = angka("Masukan panjang persegi: ")
lebar = angka("Masukan lebar persegi: ")
print("Luas persegi panjang: ", luas_persegi(panjang, lebar))

alas = angka("Masukan alas segitiga: ")
tinggi = angka("Masukan tinggi segitiga: ")
print("Luas segitiga: ", luas_segitiga(alas, tinggi))

radius = angka("Masukan radius lingkaran: ")
print("Luas lingkaran: ", luas_lingkaran(radius))
