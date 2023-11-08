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


def data_mahasiswa():
    nik = huruf("Masukan Nik: ")
    nama = huruf("Masukan Nama lengkap: ")
    umur = angka("Masukan umur: ")
    masa_kerja = angka("Masukan berapa lama kerja: ")
    gaji_pokok = floats("Masukan gaji: ")
    department = huruf("Masukan department: ")
    jabatan = huruf("Masukan jabatan: ")

    print("NIK\t\t\t:", nik)
    print("Nama\t\t:", nama)
    print("Umur\t\t:", umur)
    print("Masa kerja\t:", masa_kerja)
    print("Gaji\t\t:", gaji_pokok)
    print("Department\t:", department)
    print("Jabatan\t\t:", jabatan)


data_mahasiswa()