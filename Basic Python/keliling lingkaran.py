import math

radius = float(input('Enter The radius of a circle: '))

keliling = 2 * math.pi * radius

print(f"keliling lingkaran adalah : {keliling}cm")

# nah kan print diatas banyak banget tuh angka dibelakang koma, kita bisa nampilin cuma 2 angka di belakang coma pake round

print(f"keliling lingkaran adalah : {round(keliling, 2)}cm")

# angka 2 itu berapa angka di belakang coma yang lu mau tampilin
