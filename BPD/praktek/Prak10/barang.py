from checker import angka
from checker import huruf

global kdbrg, nmbrg, satuan, harga
def input_barang():
    print(f"\b{'Data barang': ^150}")
    print("="*100)
    print("Kode barang: ", kode)
    print("Nama barang: ", nama)
    print("Satuan: ", satuan)
    print("Harga satuan: ", harga)



kode = angka("Masukan kode barang: ")
nama = huruf("Masukan nama barang: ")
satuan = angka("Masukan Satuan: ")
harga = angka("Masukan Harga barang: ")