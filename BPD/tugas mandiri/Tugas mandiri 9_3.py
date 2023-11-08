def aritmatika(a, b, n):
    # rumus jumlah deret aritmatika: N/2 * (2A + (N - 1) * B)
    jumlah = (n / 2) * (2 * a + (n - 1) * b)
    return jumlah


suku_awal = float(input("Masukkan suku awal (A): "))
beda = float(input("Masukkan beda (B): "))
jumlah_suku = int(input("Masukkan banyaknya suku (N): "))

jumlah_deret = aritmatika(suku_awal, beda, jumlah_suku)
print(f"Jumlah deret aritmatika adalah: {jumlah_deret}")
