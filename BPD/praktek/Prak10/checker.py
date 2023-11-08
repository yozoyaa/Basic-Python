def angka(pesan):
    while True:
        try:
            return int(input(pesan))
        except ValueError:
            print("Input yang dimasukkan Salah! Gunakan Angka")


def huruf(pesan):
    while True:
        try:
            return str(input(pesan))
        except ValueError:
            print("Input yang dimasukkan Salah! Gunakan Huruf")

