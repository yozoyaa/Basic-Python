listA = []
n = int(input("Masukan jumlah B: "))
harga = 7650

for i in range(0, n):
    print("Satuan ke-{} : ".format(i + 1), (i + 1) * harga)
    elist = [i + 1], (i + 1) * harga
    listA.append(elist)
print("Elemen harga bensin adalah : \n", listA)

x = 10
while x > 1:
    y = 10
    while y >=x:
        print(x, end=" ")
        y = y - 1
    x = x - 1
    print(" ")