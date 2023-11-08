#5

nilaitk = [90, 75, 95, 85, 80]

print('=' * 100)
print(f"{'PROGRAM LIST' : ^50}")
print('=' * 100)
print('Mencetak semua isi list : ')
print(nilaitk)
print('=' * 100)
print('Mencetak isi list index ke-1')
print(nilaitk[1])
print('=' * 100)
print('Mencetak isi list mulai dari index ke-1 sampai index ke-2')
print(nilaitk[1:3])
print('=' * 100)
print('Mengambil isi list index ke-2 ke variable nilaiku')
print('nilaitk = ', nilaitk[2])
print('=' * 100)
print('\b')

#6

dictnama = {
    "Nama": "Fickry Imamsyah",
    "Umur": 20,
    "Alamat": "Jakarta selatan"
}
print("Nama saya adalah = ", dictnama.get('Nama'))
print("Umur saya adalah = ", dictnama.get('Umur'))
print("Alamat saya di = ", dictnama.get('Alamat'))