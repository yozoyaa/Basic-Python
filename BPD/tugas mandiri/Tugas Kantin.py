nama_pelanggan = input("Masukkan Nama Pelanggan: ")
jenis_pembeli = input("Pembeli (Mahasiswa atau Karyawan): ")
menu_utama = input("Masukkan Menu yang dipilih (Makanan/Minuman/Cemilan): ")

menu_makanan = ""
menu_minuman = ""
menu_cemilan = ""
harga_makanan = 0
harga_minuman = 0
harga_cemilan = 0
jumlah_pesan_makanan = 0
jumlah_pesan_minuman = 0
jumlah_pesan_cemilan = 0

if menu_utama == "Makanan":
    menu_makanan = input('Pilih Makanan (Ayam penyet/Soto ayam/Nasi goreng): ')
    if menu_makanan == "Ayam penyet":
        harga_makanan = 20000
    elif menu_makanan == "Soto ayam":
        harga_makanan = 15000
    elif menu_makanan == "Nasi goreng":
        harga_makanan = 18000
    else:
        harga_makanan = 0
    jumlah_pesan_makanan = int(input('Masukkan Jumlah Pesanan Makanan: '))

elif menu_utama == "Minuman":
    menu_minuman = input('Pilih Minuman (Teh manis/Es kopi/Nutrisar): ')
    if menu_minuman == "Teh manis":
        harga_minuman = 5000
    elif menu_minuman == "Es kopi":
        harga_minuman = 6000
    elif menu_minuman == "Nutrisar":
        harga_minuman = 4000
    else:
        harga_minuman = 0
    jumlah_pesan_minuman = int(input('Masukkan Jumlah Pesanan Minuman: '))

elif menu_utama == "Cemilan":
    menu_cemilan = input('Pilih Cemilan (Aneka gorengan/Ciki-Ciki/Basreng): ')
    if menu_cemilan == "Aneka gorengan":
        harga_cemilan = 2500
    elif menu_cemilan == "Ciki-Ciki":
        harga_cemilan = 5000
    elif menu_cemilan == "Basreng":
        harga_cemilan = 7000
    else:
        harga_cemilan = 0
    jumlah_pesan_cemilan = int(input('Masukkan Jumlah Pesanan Cemilan: '))
elif menu_utama == "Makanan Dan Minuman":
    menu_makanan = str(input('Pilih Makanan (Ayam penyet/Soto ayam/Nasi goreng): '))
    if menu_makanan == "Ayam penyet":
        harga_makanan = 20000
    elif menu_makanan == "Soto ayam":
        harga_makanan = 15000
    elif menu_makanan == "Nasi goreng":
        harga_makanan = 18000
    else:
        harga_makanan = 0
    jumlah_pesan_makanan = int(input('Masukkan Jumlah Pesanan Makanan: '))
    menu_minuman = str(input('Pilih Minuman (Teh manis/Es kopi/Nutrisar): '))
    if menu_minuman == "Teh manis":
        harga_minuman = 5000
    elif menu_minuman == "Es kopi":
        harga_minuman = 6000
    elif menu_minuman == "Nutrisari":
        harga_minuman = 4000
    else:
        harga_minuman = 0
    jumlah_pesan_minuman = int(input('Masukkan Jumlah Pesanan Minuman: '))
elif menu_utama == "Makanan, Minuman Dan Cemilan":
    menu_makanan = str(input('Pilih Makanan (Ayam penyet/Soto ayam/Nasi goreng): '))
    if menu_makanan == "Ayam penyet":
        harga_makanan = 20000
    elif menu_makanan == "Soto ayam":
        harga_makanan = 15000
    elif menu_makanan == "Nasi goreng":
        harga_makanan = 18000
    else:
        harga_makanan = 0
    jumlah_pesan_makanan = int(input('Masukkan Jumlah Pesanan Makanan: '))
    menu_minuman = str(input('Pilih Minuman (Teh manis/Es kopi/Nutrisar): '))
    if menu_minuman == "Teh manis":
        harga_minuman = 5000
    elif menu_minuman == "Es kopi":
        harga_minuman = 6000
    elif menu_minuman == "Nutrisari":
        harga_minuman = 4000
    else:
        harga_minuman = 0
    jumlah_pesan_minuman = int(input('Masukkan Jumlah Pesanan Minuman: '))
    menu_cemilan = str(input('Pilih Cemilan (Aneka gorengan/Ciki-Ciki/Basreng): '))
    if menu_cemilan == "Aneka gorengan":
        harga_cemilan = 2500
    elif menu_cemilan == "Ciki-Ciki":
        harga_cemilan = 5000
    elif menu_cemilan == "Basreng":
        harga_cemilan = 7000
    else:
        harga_cemilan = 0
    jumlah_pesan_cemilan = int(input('Masukkan Jumlah Pesanan Cemilan: '))


harga_barang = harga_makanan * jumlah_pesan_makanan + harga_minuman * jumlah_pesan_minuman + harga_cemilan * jumlah_pesan_cemilan
total_belanja = harga_barang

diskon = 0
bonus = ""
if jenis_pembeli == "Mahasiswa":
    if total_belanja >= 50000:
        diskon = total_belanja * 0.1
    if menu_makanan == "Ayam penyet" and menu_minuman == "Teh manis":
        bonus = "Gorengan 1 pcs"
    if menu_cemilan and jumlah_pesan_cemilan >= 20:
        bonus += " Es kopi"

total_bayar = total_belanja - diskon
uang_pembayaran = int(input("Berapa uang yang diberikan: "))
uang_kembalian = uang_pembayaran - total_bayar

print("\nStruk Pembayaran")
print("="*20)
print("Nama Pelanggan\t: ", nama_pelanggan)
print("Jenis Pembeli\t: ", jenis_pembeli)
print("Menu\t\t\t: ", menu_utama)
if menu_makanan:
    print("Makanan\t\t\t: ", menu_makanan)
    print("Jumlah Makanan yang dipesan: ", jumlah_pesan_makanan)
if menu_minuman:
    print("Minuman\t: ", menu_minuman)
    print("Jumlah Minuman yang dipesan: ", jumlah_pesan_minuman)
if menu_cemilan:
    print("Cemilan\t: ", menu_cemilan)
    print("Jumlah Cemilan yang dipesan: ", jumlah_pesan_cemilan)
print("Jumlah Pesanan\t: ", jumlah_pesan_makanan + jumlah_pesan_minuman + jumlah_pesan_cemilan)
print("="*20)
print("Total Belanja\t: Rp", total_belanja)
print("Diskon\t\t\t: Rp", diskon)
if bonus:
    print("Bonus\t\t: ", bonus)
print("Total Bayar\t\t: Rp", total_bayar)
print("="*20)
print("Uang Pembayaran\t: Rp", uang_pembayaran)
print("Uang Kembalian\t: Rp", uang_kembalian)
print("="*20)
