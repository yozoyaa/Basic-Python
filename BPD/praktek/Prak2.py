#1

kalimat = 'Nama saya fickry'

print(kalimat)      #mencetak string lengkap
print(kalimat[0])   #mencetak karakter pertama
print(kalimat[-1])  #mencetak karakter terakhir
print(kalimat[5:9]) #mencetak karakter dari index ke-5 sampai ke-9
print(kalimat[:4])  #mencetak karakter dari index 0 sampai ke-3

#2

bil1 = 5.15
bil2 = 25
print('nilai bil 1 adalah', bil1)
print(type(bil1))
print('nilai bil 2 adalah', bil2)
print(type(bil2))
print('nilai bil1 + bil2 adalah', bil1 + bil2)
print(type(bil1+bil2))

#3

a1 = 5
b1 = 10j
b2 = 35j

c1 = a1 + b1
c2 = b1 + b2
print(a1, '+', b1, '=', c1)
print(b1, '+', b2, '=', c1)

#4

import datetime
from datetime import timedelta

t1 = datetime.date(2018, 6, 1)
print(t1)
print('t1 = ', t1.strftime("%A, %d-%B-%Y"))

t2 = t1 + timedelta(days=5)
print('\n5 hari setelah tanggal : ', t1, 'adalah', t2)
print(t2.strftime("t2 = %A, %d-%B-%Y"))

#5

nilai = 5 > 10
nilai2 = 10 > 5
huruf = 'hello' == 'hello'

print(nilai)
print(nilai2)
print(huruf)

#6

a = [5,10,15,20,25,30,35,40]

#mecetak item dari index ke-2
print("a[2] = ", a[2])

#mencetak item dari index ke 0 sampai ke-2
print(a[0:3])

#mencetak item mulai dari index ke-5 sampai akhir
print(a[5:])

#mencetak item mulai dari index ke-0 sampai index ke-4
print(a[:5])

print(len(a))

#7

data = ('a', 'b', 'c', 'd', 1,2,3,4,)

#mengakses data paling peratama
print(data[0])

#mengakses nilai dari index ke-3 sampai index akhir
print(data[3:])

#mengakses nilai dari index ke-0 sampai index ke-2
print(data[:3])

#mengakses nilai dari index ke-2 sampai index ke-6
print(data[2:6])

#mengakses data paling terakhir
print(data[-1])

#8

# set dengan nilai campuran

data = {'a', 'b', 'c', 'd', 1, 2, 3, 4}
print(data)

# set tidak menampung nilai yang sama
x = {1, 2, 3, 4, 1, 2, 3, 4}
print(x)

#9

#tipe data dictionary
data_mhs = {'nama1': 'Zara', 'Agel': 17, 'class1': '1A',
            'Nama2': 'Joko', 'Age2': 19, 'Class2': 'B1',
            'Nama3': 'Wawan', 'Age3': 21, 'Class3': 'C3'}
print(data_mhs['Nama2'] + data_mhs['class1'])
print(data_mhs['Age2'])

#10

var1 = 'hello everyone'
var2 = 'i love you, naya'
print(var1[0])
print(var2[2:6])
print(var1[:6] + 'world')
