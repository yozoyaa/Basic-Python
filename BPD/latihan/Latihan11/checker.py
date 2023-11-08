def angka(pesan):
    while True:
        try:
            return int(input(pesan))
        except ValueError:
            print("Input yang dimasukan salah! silahkan coba lagi")


def huruf(pesan):
    while True:
        try:
            return str(input(pesan))
        except ValueError:
            print("Input yang dimasukan salah!, silahkan coba lagi")


def floats(pesan):
    while True:
        try:
            return float(input(pesan))
        except ValueError:
            print("Input yang dimasukan salah!, silahkan coba lagi")