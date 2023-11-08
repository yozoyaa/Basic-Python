# Fungsi untuk menemukan harga terendah dari tiga harga produk
def harga_terendah_dari_tiga(harga1, harga2, harga3):
    # Menggunakan fungsi min() untuk mendapatkan harga terendah
    return min(harga1, harga2, harga3)

# Fungsi untuk meminta input harga dan memvalidasinya
def minta_input_harga():
    while True:
        try:
            # Input harga produk dan konversi ke integer
            harga = int(input("Masukkan harga produk: "))
            return harga
        except ValueError:
            print("Input tidak valid, silakan masukkan angka bulat.")

# Input harga produk dengan validasi
harga_produk1 = minta_input_harga()
harga_produk2 = minta_input_harga()
harga_produk3 = minta_input_harga()

# Mendapatkan harga terendah
harga_terendah = harga_terendah_dari_tiga(harga_produk1, harga_produk2, harga_produk3)

# Output harga terendah
print(f"Harga produk terendah adalah: {harga_terendah}")