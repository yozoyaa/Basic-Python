from inputnilai import input_nilai
from rumus import hitung_nilai_akhir
from predikat import get_predikat
from grade import get_grade

data_mahasiswa = input_nilai()

nilai_akhir = hitung_nilai_akhir(data_mahasiswa)

grade = get_grade(nilai_akhir)

predikat = get_predikat(grade)

print("\n")
print("="*40)
print("PROGRAM HITUNG NILAI MAHASISWA")
print("="*40)
print(f"Nama Mahasiswa\t\t\t: {data_mahasiswa['nama']}")
print(f"Nilai UTS\t\t\t\t: {data_mahasiswa['nilai_uts']}")
print(f"Nilai UAS\t\t\t\t: {data_mahasiswa['nilai_uas']}")
print(f"Nilai Quiz\t\t\t\t: {data_mahasiswa['nilai_quiz']}")
print("="*40)
print(f"Banyaknya Tugas\t\t\t: {data_mahasiswa['jumlah_tugas']}")
for i, nilai in enumerate(data_mahasiswa['nilai_tugas'], 1):
    print(f"Nilai Tugas {i}\t\t\t: {nilai}")
print("="*40)
print(f"Rata-rata Nilai Tugas\t: {sum(data_mahasiswa['nilai_tugas']) / len(data_mahasiswa['nilai_tugas']):.2f}")
print(f"Nilai Akhir\t\t\t\t: {nilai_akhir:.2f}")
print(f"Grade\t\t\t\t\t: {grade}")
print(f"Predikat\t\t\t\t: {predikat}")
print("="*40)
