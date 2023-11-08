#3.1 praktikum

nama = "fickry"
print(nama)
print(type(nama))
umur1 = "dua puluh"
print(umur1)
print(type(umur1))

nama_depan = "Fickry"
nama_belakang = "Imamsyah"
nama = nama_depan + " " + nama_belakang
umur = 20
hobi = "nyari duit"
print("biodata\n")
print("nama : ", nama,"\numur : ", umur)
print("hobi : ", hobi)

inivariable = "awaw"
ini_variable = "wewe"
_inivar = 12121
inivariable1010 = "gitudah"

panjang = 10
lebar = 20
luas = panjang + lebar

print(luas)

#3.2

#tipe data bool
print(True)

#tipe data string
print("aoifaoaw")
print("apfinawpfiaw")

#tipe data integer
print(1212)
print(2526236)

#tipe data float
print(1321.1212)
print(654654.1313)

#tipe data complex
print(2j)

#tipe data list
print([1,2,3,4,5])
print(["satu", "dua", "tiga", "empat", "lima"])

#tipe data tuple
print((1,2,3,5,6))
print(("satu", "dua", "tiga", "empat"))

#tipe data dictionary
print({"nama":"budi", 'umur': 20})

biodata = {"nama":"budi", 'umur': 20}
print(biodata)
print(type(biodata))

#3.3

#list kosong
list_kosong = []

#list str
list_buah = ['pisang', 'mangga']

#list int
list_nilai = [20, 40, 60, 70]

#list campuran tipe data
list_jawaban = [150, 33.33, 'presiden ku megawati', False]

#3.4

x = 10
y = 20

print('x berisi angka : ',x ,'desimal atau',bin(x), 'biner')
print('y berisi angka : ',y ,'desimal atau',bin(y), 'biner')

print("\n")

print('x & y : ', x & y)
print('x | y : ', x | y)
print('x ^ y : ', x ^ y)
print('~x    : ',~x)
print('x << 1 : ',x << 1)
print('x >> 1 : ',x >> 1)

#3.5
print('Hasil dari true and true', True and True)
print('Hasil dari true and false', True and False)
print('Hasil dari false and true', False and True)
print('Hasil dari false and false', False and True)

print("\n")

print('Hasil dari not true : ', not True)
print('Hasil dari no false : ', not False)

hasil = (5 > 6) and (10 <= 8)
print(hasil)

hasil1 = ('Budi luhur' == 'Budi luhur') or (10 <= 8)
print(hasil1)

hasil2 = not (10 < 10)
print(hasil2)

hasil3 = ('Budi luhur' == 'Budi luhur') and (10 <= 8) or (1 != 1)
print(hasil3)

a = 5
b = 5
c = 6
print('a is b : ', a is b)
print('a is c : ', a is c)
print('a is not c : ', a is not c)
print("\n")

i = 'budi luhur'
j = 'budi luhur'
print('i is not j :', i is not j)
print('i is j :', i is j)
print("\n")