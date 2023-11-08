from checker import angka
from persegi_panjang import luas_persegi
from segitiga import luas_segitiga
from lingkaran import luas_lingkaran

def main():
    panjang = angka("Masukan panjang persegi: ")
    lebar = angka("Masukan lebar persegi: ")
    print("Luas persegi panjang: ", luas_persegi(panjang, lebar))

    alas = angka("Masukan alas segitiga: ")
    tinggi = angka("Masukan tinggi segitiga: ")
    print("Luas segitiga: ", luas_segitiga(alas, tinggi))

    radius = angka("Masukan radius lingkaran: ")
    print("Luas lingkaran: ", luas_lingkaran(radius))

if __name__ == '__main__':
    main()