def angka(pesan):
    while True:
        try:
            return int(input(pesan))
        except ValueError:
            print("Input yang dimasukan salah!, masukan angka")

def huruf(pesan):
    while True:
        try:
            return str(input(pesan))
        except ValueError:
            print("Input yang dimasukan salah!, masukan angka")


def inputdata(N):
    datamhs = []
    for i in range(N):
        print(f"Masukkan data mahasiswa ke- {i + 1}: ")
        nim = angka("Masukan nim: ")
        nama = huruf("Masukan nama: ")
        jurusan = huruf("Masukan nama jurusan: ")
        telepon = huruf("Masukan nomor telepon: ")
        datamhs.append((nim, nama, jurusan, telepon))
    return datamhs


def proses(X):
    return X


def cetakhasil(data):
    print("\n Daftar Mahasiswa: ")
    for nim, nama, jurusan, telepon in data:
        print(f"Nim\t\t\t: {nim}")
        print(f"Nama\t\t: {nama}")
        print(f"Jurusan\t\t: {jurusan}")
        print(f"Telepon\t\t: {telepon}")
        print("-" * 20)


def main():
    N = angka("Berapa banyak data mahasiswa? ")
    datamhs = inputdata(N)
    data_diproses = proses(datamhs)
    cetakhasil(data_diproses)


if __name__ == "__main__":
    main()