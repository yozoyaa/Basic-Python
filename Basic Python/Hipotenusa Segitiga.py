import math

# jadi kita nyari sisi terpanjang dari segitiga siku siku ya ges

a = float(input(f"Enter sisi A: "))
b = float(input(f"Enter sisi B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Sisi C = {round(c, 2)}cm")
