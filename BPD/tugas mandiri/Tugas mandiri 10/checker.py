def huruf(pesan):
    while True:
        try:
            return str(input(pesan))
        except ValueError:
            print("Input yang dimasukan salah! gunakan huruf")


def angka(pesan):
    while True:
        try:
            return int(input(pesan))
        except ValueError:
            print("Input yang dimasukan salah! gunakan angka")