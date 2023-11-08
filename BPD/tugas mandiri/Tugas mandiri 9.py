def angka(pesan):
    while True:
        try:
            return int(input(pesan))
        except ValueError:
            print("Input yang dimasukan salah! Gunakan angka")


def inputdata(N):
    index = []
    print(f"Masukan {N} bilangan : ")
    for _ in range(N):
        no_index = angka("> ")
        index.append(no_index)
    return index


def proses(X, index):
    return [no_index for no_index in index if no_index % X == 0]


def cetakhasil(ix):
    print("bilangan kelipatan dari X")
    for no_index in ix:
        print(no_index, end=" ")
    print()


def main():
    N = angka("Berapa banyak no index? ")
    index = inputdata(N)
    X = angka("Masukan bilangan untuk kelipatan yang diinginkan (X): ")
    hasil = proses(X, index)
    cetakhasil(hasil)


if __name__ == "__main__":
    main()
