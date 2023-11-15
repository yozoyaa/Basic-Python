def angka(pesan):
    while True:
        try:
            return int(input(pesan))
        except ValueError:
            print("Input yang dimasukkan salah! Masukkan angka!")


def input_nama():
    return input("Masukan Nama: ")


def kelas_tujuan():
    return input("Masukan Kelas (Ekonomi/Bisnis/Vip): ")


def harga_tiket(kota, kelas):
    harga = {
        ("Cirebon", "Ekonomi"): 120000,
        ("Semarang", "Ekonomi"): 180000,
        ("Solo", "Ekonomi"): 250000,
        ("Yogyakarta", "Ekonomi"): 280000,
        ("Surabaya", "Ekonomi"): 320000,
        ("Cirebon", "Bisnis"): 150000,
        ("Semarang", "Bisnis"): 200000,
        ("Solo", "Bisnis"): 285000,
        ("Yogyakarta", "Bisnis"): 310000,
        ("Surabaya", "Bisnis"): 375000,
        ("Cirebon", "Vip"): 180000,
        ("Semarang", "Vip"): 230000,
        ("Solo", "Vip"): 325000,
        ("Yogyakarta", "Vip"): 360000,
        ("Surabaya", "Vip"): 400000
    }
    return harga.get((kota, kelas), "Value error")


def kota_tujuan(code):
    kota = {
        1: "Cirebon",
        2: "Semarang",
        3: "Solo",
        4: "Yogyakarta",
        5: "Surabaya"
    }
    return kota.get(code, "Value Error")


code = angka("Masukan Code Tujuan: ")
nama = input_nama()
kelas = kelas_tujuan()
kota = kota_tujuan(code)
jumlah = angka("Berapa banyak jumlah tiket yang ingin dipesan: ")
harga_per_tiket = harga_tiket(kota, kelas)
total = harga_per_tiket + jumlah

if harga_per_tiket == "Value error":
    print("Kombinasi kota dan kelas tidak valid.")
else:
    total = harga_per_tiket * jumlah
    diskon = 0
    if kelas == "Vip":
        diskon = int(total * 0.15)
        total -= diskon

    bayar = angka("Masukan berapa uang yang dibayar: ")

    print(f"{'=' * 10} {'Program Pemesanan Tiket BUS'} {'=' * 10}")
    print("\nNama Pemesan\t:", nama)
    print("Tujuan\t\t\t:", kota)
    print("Kelas Bus\t\t:", kelas)
    print("Harga Tiket\t\t:", harga_per_tiket)
    print("Jumlah tiket dipesan:", jumlah)
    print("Total\t\t\t:", total)
    if diskon:
        print("Potongan\t\t:", diskon)
    print("Jumlah bayar\t:", bayar)
