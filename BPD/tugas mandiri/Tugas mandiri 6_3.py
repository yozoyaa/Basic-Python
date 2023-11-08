def minta_input_float(pesan):
    while True:
        try:
            return float(input(pesan))
        except ValueError:
            print("Input tidak valid, silakan masukkan angka.")


def minta_input_integer(pesan):
    while True:
        try:
            return int(input(pesan))
        except ValueError:
            print("Input tidak valid, silakan masukkan bilangan bulat.")


def hitung_diskon(lama_member, biaya_layanan):
    if lama_member >= 20:
        return 0.15 * biaya_layanan
    elif lama_member >= 10:
        return 0.10 * biaya_layanan
    elif lama_member >= 5:
        return 0.05 * biaya_layanan
    else:
        return 0


def main():
    kode_member = input("Masukkan kode member: ")
    nama_member = input("Masukkan nama member: ")
    biaya_layanan = minta_input_float("Masukkan biaya layanan: ")
    lama_member = minta_input_integer("Lama menjadi member (tahun): ")

    diskon = hitung_diskon(lama_member, biaya_layanan)
    harga_final = biaya_layanan - diskon

    print(f"Member dengan kode {kode_member} dan nama {nama_member} mendapatkan diskon: {diskon}")
    print(f"Harga layanan setelah diskon: {harga_final}")


if __name__ == "__main__":
    main()