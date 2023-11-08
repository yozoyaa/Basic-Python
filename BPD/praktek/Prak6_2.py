nip = input("Masukan ID Number: ")
nama_pegawai = input("Masukan Nama: ")
gaji_pokok = int(input("Masukan Gaji: "))
lama_kerja = int(input("Masukan Lama kerja: "))
golongan = input("Masukan golongan kerja: ")

if golongan in("C", "D"):
    if lama_kerja >= 20:
        komisi = (10/100) * gaji_pokok
    elif lama_kerja >= 10:
        komisi = (5/100) * gaji_pokok
    else:
        komisi = 0
elif golongan in("A", "B"):
    if lama_kerja >= 20:
        komisi = (5/100) * gaji_pokok
    elif lama_kerja >= 10:
        komisi = (3/100) * gaji_pokok
    else:
        komisi = 0
else:
    komisi = 0

total_gaji = float(gaji_pokok) + komisi

print("\n Data gaji pegawai")
print("="*20)
print("NIP: ", nip)
print("Nama Pegawai: ", nama_pegawai)
print("Gaji pokok: ", gaji_pokok)
print("Komisi: ", komisi)
print("Total gaji: ", total_gaji)