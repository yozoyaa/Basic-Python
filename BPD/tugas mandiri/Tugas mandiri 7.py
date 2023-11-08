# Start from 10 and go up to and including 100, in steps of 10
for i in range(100, 54, -5):
    print(i, end=" ")
print("\n")
for i in range(10, 101, 10):
    print(i, end=" ")
print("\n")
for i in range(11):
    number = 2 ** i
    print(number, end=" ")
print("\n")
uang_awal = 1000000
bunga = 2
jumlah_bulan = 10

for bulan in range(jumlah_bulan):
    uang_awal += (uang_awal * bunga / 100)

print(f"Jumlah uang setelah {jumlah_bulan} bulan adalah: Rp. {uang_awal:.2f}")
