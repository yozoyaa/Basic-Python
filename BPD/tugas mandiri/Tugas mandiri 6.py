# Fungsi untuk menemukan harga terendah dari tiga harga produk
def harga_terendah_dari_tiga(harga1, harga2, harga3):
    # Menggunakan fungsi min() untuk mendapatkan harga terendah
    return min(harga1, harga2, harga3)

# Input harga produk
harga_produk1 = int(input("Masukkan harga produk pertama: "))
harga_produk2 = int(input("Masukkan harga produk kedua: "))
harga_produk3 = int(input("Masukkan harga produk ketiga: "))

# Mendapatkan harga terendah
harga_terendah = harga_terendah_dari_tiga(harga_produk1, harga_produk2, harga_produk3)

# Output harga terendah
print(f"Harga produk terendah adalah: {harga_terendah}")