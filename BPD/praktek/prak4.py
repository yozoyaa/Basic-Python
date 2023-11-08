#1

nama = 'Fickry imamsyah'
usia = 20
sudah_menikah = False

print(nama)
print(usia)
print(sudah_menikah)

#2

nama = 'Fickry imamsyah'
usia = 20
sudah_menikah = False

print(nama)
print(usia)
print(sudah_menikah)

print(type(nama))
print(type(usia))
print(type(sudah_menikah))

#3

nama = 'fickry imamasya'
print(nama)

umur = 20
print(umur)
print(type(umur))
umur1 = 'dua puluh'
print(umur1)
print(type(umur1))

inivariable = 'hello'
ini_juga_variable = 'hello'
_inivariable = 'hello'
inivariable22 = 'hello'

panjang = 10
lebar = 5
luas = panjang + lebar
print(luas)

#4
# tipe data boolean
print(True)
# tipe data string
print('olaghnawopghaw')
print("pahifgpawohgpawg")
# tipe data int
print(20)
# tipe data float
print(3.14)
# tipe data complex
print(5j)
# tipe data list
print([1, 2, 3, 4, 5])
print(['satu', 'dua', 'tiga'])
# tipe data tuple
print((1, 2, 3, 4, 5))
print(('satu', 'dua', 'tiga'))
# tipe data dict
print({"nama": "Budi", 'umuir': 20})
# tipe data dict dimasukan ke dalama variable
biodata = {"nama": "Budi", 'umuir': 20}

#5

#list kosong
list_kosong = []

# list yang berisi kumpulan string
list_buah = ['aawoikfhnp', 'apgwhnjapow', 'awvonaw']

# list yang berisi kumpulan integer
list_angka = [1, 2, 3, 5, 6]

# list yang berisi campuran tipe data
list_jawaban = [150, 1, 233.44, 'woagwfwioan', True]

#6

#list kosong
list_kosong1 = []

# list yang berisi kumpulan string
list_buah1 = ['aawoikfhnp', 'apgwhnjapow', 'awvonaw']

# list yang berisi kumpulan integer
list_angka1 = [1, 2, 3, 5, 6]

# list yang berisi campuran tipe data
list_jawaban1 = [150, 1, 233.44, 'woagwfwioan', True]

# cetak isi seluruh list
print(list_buah1)
print(list_kosong1)
print(list_jawaban1)
print(list_angka1)

# cetak isi list tertentu
print(list_buah1[0])
print(list_jawaban1[2])
print(list_angka1[3])

# cetak isi list menggunakan index negatif untuk mencetak dari belakang
print(list_buah1[-1])
print(list_jawaban1[-3])
print(list_angka1[-4])

#7

x = 10
y = 12

print('x berisi angka', x, 'desimal atau', bin(x), 'biner')
print('y berisi angka', y, 'desimal atau', bin(y), 'biner')

print('\n')

print('x & y : ', x & y)
print('x | y : ', x | y)
print('x ^ y : ', x ^ y)
print('~x\t', ~x)
print('x << 1 : ', x << 1)
print('x >> 1 : ', x >> 1)

#8

print(True and True)
print(True and False)
print(False and True)
print(False and False)

print('\n')

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print('\n')

print(not True)
print(not False)

hasil = (5 > 6) and (10 << 8)
print(hasil)

hasil = ('budiluhur' == 'budiluhur') or (10 << 8)
print(hasil)

hasil = not (10 < 10)
print(hasil)

hasil = ('budiluhur' == 'budiluhur') and (10 <= 8) or (1 != 1)
print(hasil)

#9

a = 5
b = 5
c = 6
print('a is b :', a is b)
print('a is c :', a is c)
print('a is not c :', a is not c)
print('\n')

i = 'budiluhur'
j = 'budiluhur'
print('i is j :', i is j)
print('i is not j :', i is not j)
print('\n')

x = ['a', 'b', 'c']
y = ['a', 'b', 'c']
print('x is y : ', x is y)
print('x is not y : ', x is not y)
print('\n')

#10

foo = 'budiluhur'
print(foo)
print('\'i\' in foo : ', 'i' in foo)
print('k' not in foo)
print('d' not in foo)
print('\n')

bar = ['a', 'b', 'c']
print('bar: ', bar)
print('a' in bar)
print('a' not in bar)
print('d' not in bar)

baz = (12, 43, 102, 55)
print('baz: ', baz)
print(102 in bar)
print(102 not in bar)
print(35 in bar)
print('\n')

#11

print(11 == 11)
print("CodeSya" != "Python")
print(5 >= 0)
print("HODOR" == "hodor")
print(100 < (10*10))

#12

# penugasan pertama
a = 10
print('a = 10 -> ', a)
a += 5 # tambah sama dengan
print('a += 5 -> ', a)
a -= 3 # kurang sama dengan
print('a -= 3 -> ', a)
a *= 6 # kali sama dengan
print('a *= 6 -> ', a)
a /= 8 # bagi sama dengan
print('a /= 8 -> ', a)
print('\n')

# karena a jadi float, kita ubah lagi menjadi integer
a = int(a)

a %= 9 # sisa bagi sama dengan
print('a %= 9 -> ', a)
a //= 6 # pembagian bulat sama dengan
print('a //= 6 -> ', a)
a **= 1 # pangkat sama dengan
print('a **= 1 -> ', a)

a &= 2
print('a &= 2 -> ', a)
a != 3
print('a != 3 -> ', a)
a ^= 4
print('a ^= 4 -> ', a)
a >>= 4
print('a >>= 4 -> ', a)
a <<= 2
print('a <<= 2 -> ', a)

