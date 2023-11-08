def angka(pesan):
    while True:
        try:
            return float(input(pesan))
        except ValueError:
            print("Input yang dimasukan salah! Masukan Angka")