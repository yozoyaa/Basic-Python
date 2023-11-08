from checker import angka
from checker import huruf

global kdbrg, nmbrg, satuan, harga
def input_pelanggan():
    print(f"\b{'Data pelanggan': ^150}")
    print("="*100)
    print("Kode Pelanggan: ", kode)
    print("Nama Pelanggan: ", nama)
    print("Alamat: ", alamat)
    print("Nomor HP: ", nohp)


kode = angka("Masukan Kode pelanggan: ")
nama = huruf("Masukan nama pelanggan: ")
alamat = huruf("Masukan alamat: ")
nohp = huruf("Masukan Nomor HP: ")