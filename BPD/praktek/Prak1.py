# print

# (end="") digunakan untuk tidak mencetak garis baru

print("halo ", end="")
print("apa kabar? ", end="")
print("ganteng")
print("")

# "\n" digunakan untuk mencetak 2 garis baru, dimana yang pertama dari perintah print itu sendiri
# "\t" digunakan untuk mencetak tab ke kanan sebanyak 1 kali

a = "selamat pagi"
print(a, "\n") #
b = "selamat siang"
print(b)
print("\n")
c = "selamat malam"
print(c, "\n")

x = "no."
y = "Fickry"
z = "2324215625"
print(x, "\t", y, "\t\t", z)
print("\n")
# Variable

myVar = "ganteng" # str untuk print kata
print(myVar)
print(type(myVar)) # Print class <class 'str'>

Number = 2020 # int untuk angka
print(Number)
print(type(Number)) # Print class <class 'int'>

Decimal = 205.5 # Float untuk angka decimal
print(Decimal)
print(type(Decimal)) # print class <class 'float'>

bool = True # true or false
print(bool)
print(type(bool)) # print class <class 'bool'>
print("\n")
# basic penjumlahan

panjang = 20
lebar = 10
print(panjang, " x ", lebar, "=", panjang + lebar)

panjang = 50
lebar = 10
luas = panjang * lebar
print("%i x %i = %i "% (panjang, lebar, luas))
print("\n")

#basic table print

myTable = ["Tata tertib kuliah", "===============================", "1. tidak ada titip absen", "\a 2. kehadiran dievaluasi", "\n3. pakaian layak di kampus", "\n4. toleransi terlambat hadir 10 menit", "5. tidak ada tugas atau pr susulan"]
for row in myTable:
    print(row)

print("\n")

a = 270
print("%o"% (a))
print("%x"% (a))
print("%s"% (a))
print("%c"% (a))
print("%g"% (a))