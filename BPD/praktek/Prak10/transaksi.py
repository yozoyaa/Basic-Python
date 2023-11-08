import pelanggan
import barang
from checker import angka
from checker import huruf

global notrans, tgltrans, kdbrg, nmbrg, harga, jumlah
def input_transaksi():
    print(f"\n{'Data Transaksi Penjualan': ^150}")
    print("="*100)
    print("Nomor transaksi: ", notrans)
    print("Tanggal Transaksi: ", tgltrans)

    pelanggan.input_pelanggan()

    barang.input_barang()
    harga = int(barang.harga)
    print("Jumlah pesan: ", jumlah)
    totalhrg = harga * jumlah
    print("Total Harga: ", totalhrg)


notrans = huruf("Masukan nomor Transaksi: ")
tgltrans = huruf("Masukan Tanggal Transaksi: ")
jumlah = angka("Masukan Jumlah Pesanan: ")