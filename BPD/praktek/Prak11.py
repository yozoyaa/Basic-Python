number = 1
while number != -1:
    try:
        number = int(input("Masukan Angka: "))
        print("Anda memasukan: ", number)
        break
    except ValueError:
        print("Bukan angka bilangan integer!")
