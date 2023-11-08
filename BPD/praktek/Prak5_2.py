#5.2

nip = input("NIP : ")
nama_pegawai = input("Nama Pegawai : ")
gaji_pokok = input("Gaji pokok : ")

komisi = float(3.5/100) * float(gaji_pokok)
total_gaji = float(gaji_pokok) + (komisi)

print("\n")
print("Nama : ", nama_pegawai)
print("NIP", nip)
print("Komisi yang didapat : ", komisi)
print("Total Gaji : ", total_gaji)