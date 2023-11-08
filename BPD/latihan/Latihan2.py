#1

nama = 'Fickry'
pesan = 'janganlah berjudi'
print(nama[0])
print(pesan[0:6])
print(pesan[:17])
print(pesan[10:])
print(len(pesan))

#2

import datetime

nama_depan = 'fickry'
nama_belakang = 'imamsyah'
nama_lengkap = nama_depan + nama_belakang
tgllahir = datetime.datetime(2002, 12, 10)
usia = 20
alamat = 'jakarta selatan'
kata_mutiara = 'carilah uang sebanyak-banyaknya'

print(nama_lengkap, tgllahir, 'usia : ', usia, 'tahun', alamat, 'Kata mutiara : ', kata_mutiara)

print(type(nama_lengkap))
print(type(tgllahir))
print(type(usia))
print(type(alamat))
print(type(kata_mutiara))

#3

list_buah = ['jeruk', 'mangga', 'semangka', 'apel']
list_angka = [1, 2, 3, 4, 5, 6, 7]

print(list_buah[0:1])
print(list_angka[0:2])
print(list_buah[1:3])
print(list_angka[0:-1])
print(list_buah[1:3])
print(list_angka[1:3])
print(list_buah[-3:-1])

#4
tup1 = ('fisika', 'kimia', 1993, 2018, 1, 2, 3, 4)

print(type(tup1))
print(tup1[0:2])
print(tup1[:3])
print(tup1[5:])
print(tup1[-1:3])
print(tup1[-3:-1])

#5

A = {2, 3, 5, 1, 7}
B = {4, 5, 2, 7, 2}

print(A | B)

A.union(B)
print(A.union(B))

#6

student = {
    "nama": "Fickry",
    "Umur": 20,
    "Tinggi": 175.2,
    "Hobi": ["Olahraga", "Cari uang"],
    "Kontak": {
        "website": "fiikriimamsyah.com",
        "email": "fikriimamsyah477@gmail.com"
    }
}
print("Nama : ", student.get('nama'))
print("Umur : ", student.get('Umur'))
print("Tinggi : ", student.get('Tinggi'))
print("Hobi : ", student.get('Hobi'))
print("Kontak : ", student.get('Kontak'))

