from pendaftaran import tambah_mahasiswa, cetak_mahasiswa


def input_mahasiswa():
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama Lengkap: ")
    no_hp = input("Masukkan No. HP: ")
    email = input("Masukkan Email: ")
    alamat = input("Masukkan Alamat: ")
    nem = input("Masukkan NEM: ")

    tambah_mahasiswa(nim, nama, no_hp, email, alamat, nem)


def main():
    while True:
        input_mahasiswa()
        cetak_mahasiswa()
        lanjut = input("Tambahkan mahasiswa lain? (y/n): ")
        if lanjut.lower() != 'y':
            break


if __name__ == "__main__":
    main()
