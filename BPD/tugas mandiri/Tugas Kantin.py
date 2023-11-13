nama_pelanggan = input("Masukkan Nama Pelanggan: ")
jenis_pembeli = input("Pembeli (Mahasiswa atau Karyawan): ")
menu_utama = input("Masukkan Menu yang dipilih (Makanan/Minuman/Cemilan): ")

nama_pelanggan = nama_pelanggan.lower()
jenis_pembeli = jenis_pembeli.lower()
menu_utama = menu_utama.lower()

menu_makanan = ""
menu_minuman = ""
menu_cemilan = ""
harga_makanan = 0
harga_minuman = 0
harga_cemilan = 0
jumlah_pesan_makanan = 0
jumlah_pesan_minuman = 0
jumlah_pesan_cemilan = 0

if menu_utama == "makanan":
    menu_makanan = input('Pilih Makanan (Ayam penyet/Soto ayam/Nasi goreng): ')
    if menu_makanan == "ayam penyet":
        harga_makanan = 20000
    elif menu_makanan == "soto ayam":
        harga_makanan = 15000
    elif menu_makanan == "nasi goreng":
        harga_makanan = 18000
    else:
        harga_makanan = 0
    jumlah_pesan_makanan = int(input('Masukkan Jumlah Pesanan Makanan: '))

elif menu_utama == "minuman":
    menu_minuman = input('Pilih Minuman (Teh manis/Es kopi/Nutrisar): ')
    if menu_minuman == "teh manis":
        harga_minuman = 5000
    elif menu_minuman == "es kopi":
        harga_minuman = 6000
    elif menu_minuman == "nutrisar":
        harga_minuman = 4000
    else:
        harga_minuman = 0
    jumlah_pesan_minuman = int(input('Masukkan Jumlah Pesanan Minuman: '))

elif menu_utama == "cemilan":
    menu_cemilan = input('Pilih Cemilan (Aneka gorengan/Ciki-Ciki/Basreng): ')
    if menu_cemilan == "aneka gorengan":
        harga_cemilan = 2500
    elif menu_cemilan == "ciki ciki":
        harga_cemilan = 5000
    elif menu_cemilan == "basreng":
        harga_cemilan = 7000
    else:
        harga_cemilan = 0
    jumlah_pesan_cemilan = int(input('Masukkan Jumlah Pesanan Cemilan: '))
elif menu_utama == "makanan dan minuman":
    menu_makanan = str(input('Pilih Makanan (Ayam penyet/Soto ayam/Nasi goreng): '))
    if menu_makanan == "ayam penyet":
        harga_makanan = 20000
    elif menu_makanan == "soto ayam":
        harga_makanan = 15000
    elif menu_makanan == "nasi goreng":
        harga_makanan = 18000
    else:
        harga_makanan = 0
    jumlah_pesan_makanan = int(input('Masukkan Jumlah Pesanan Makanan: '))
    menu_minuman = str(input('Pilih Minuman (Teh manis/Es kopi/Nutrisar): '))
    if menu_minuman == "teh manis":
        harga_minuman = 5000
    elif menu_minuman == "es kopi":
        harga_minuman = 6000
    elif menu_minuman == "nutrisari":
        harga_minuman = 4000
    else:
        harga_minuman = 0
    jumlah_pesan_minuman = int(input('Masukkan Jumlah Pesanan Minuman: '))
elif menu_utama == "makanan, minuman dan cemilan":
    menu_makanan = str(input('Pilih Makanan (Ayam penyet/Soto ayam/Nasi goreng): '))
    if menu_makanan == "ayam penyet":
        harga_makanan = 20000
    elif menu_makanan == "soto ayam":
        harga_makanan = 15000
    elif menu_makanan == "nasi goreng":
        harga_makanan = 18000
    else:
        harga_makanan = 0
    jumlah_pesan_makanan = int(input('Masukkan Jumlah Pesanan Makanan: '))
    menu_minuman = str(input('Pilih Minuman (Teh manis/Es kopi/Nutrisar): '))
    if menu_minuman == "teh manis":
        harga_minuman = 5000
    elif menu_minuman == "es kopi":
        harga_minuman = 6000
    elif menu_minuman == "nutrisari":
        harga_minuman = 4000
    else:
        harga_minuman = 0
    jumlah_pesan_minuman = int(input('Masukkan Jumlah Pesanan Minuman: '))
    menu_cemilan = str(input('Pilih Cemilan (Aneka gorengan/Ciki-Ciki/Basreng): '))
    if menu_cemilan == "aneka gorengan":
        harga_cemilan = 2500
    elif menu_cemilan == "ciki ciki":
        harga_cemilan = 5000
    elif menu_cemilan == "basreng":
        harga_cemilan = 7000
    else:
        harga_cemilan = 0
    jumlah_pesan_cemilan = int(input('Masukkan Jumlah Pesanan Cemilan: '))

menu_makanan = menu_makanan.lower()
menu_minuman = menu_minuman.lower()
menu_cemilan = menu_cemilan.lower()

harga_barang = (int(harga_makanan * jumlah_pesan_makanan) + int(harga_minuman * jumlah_pesan_minuman)
                + int(harga_cemilan * jumlah_pesan_cemilan))
total_belanja = harga_barang

diskon = 0
bonus = ""
if jenis_pembeli == "mahasiswa":
    if total_belanja >= 50000:
        diskon = total_belanja * 0.1
    if menu_makanan == "ayam penyet" and menu_minuman == "teh manis":
        bonus = "gorengan 1 pcs"
    if menu_cemilan and jumlah_pesan_cemilan >= 20:
        bonus += " Es kopi"

total_bayar = total_belanja - diskon
uang_pembayaran = int(input("Berapa uang yang diberikan: "))
uang_kembalian = uang_pembayaran - total_bayar

print(f"\n{'Struk Pembayaran': ^50}")
print("="*50)
print("Nama Pelanggan\t\t\t\t: ", nama_pelanggan)
print("Jenis Pembeli\t\t\t\t: ", jenis_pembeli)
print("Menu\t\t\t\t\t\t: ", menu_utama)
if menu_makanan:
    print("Makanan\t\t\t\t\t\t: ", menu_makanan)
    print("Jumlah Makanan yang dipesan\t: ", jumlah_pesan_makanan)
if menu_minuman:
    print("Minuman\t\t\t\t\t\t: ", menu_minuman)
    print("Jumlah Minuman yang dipesan\t: ", jumlah_pesan_minuman)
if menu_cemilan:
    print("Cemilan\t\t\t\t\t\t: ", menu_cemilan)
    print("Jumlah Cemilan yang dipesan\t: ", jumlah_pesan_cemilan)
print("Jumlah Pesanan\t\t\t\t: ", jumlah_pesan_makanan + jumlah_pesan_minuman + jumlah_pesan_cemilan)
print("="*50)
print("Total Belanja\t\t\t\t: Rp", total_belanja)
print("Diskon\t\t\t\t\t\t: Rp", diskon)
if bonus:
    print("Bonus\t\t\t\t\t\t: ", bonus)
print("Total Bayar\t\t\t\t\t: Rp", total_bayar)
print("="*50)
print("Uang Pembayaran\t\t\t\t: Rp", uang_pembayaran)
print("Uang Kembalian\t\t\t\t: Rp", uang_kembalian)
print("="*50)
