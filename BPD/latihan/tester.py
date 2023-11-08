jumlah_tugas = int(input("Masukkan jumlah tugas yang diberikan: "))
nilai_tugas = []
for i in range(jumlah_tugas):
    nilai = float(input(f"Masukkan nilai tugas ke-{i+1}: "))
    nilai_tugas.append(nilai)

rata_rata = sum(nilai_tugas) / jumlah_tugas

print(f"Rata-rata nilai tugas adalah: {rata_rata:.2f}")
