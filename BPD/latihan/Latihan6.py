presensi = input("nilai presensi : ")
tugas = input("nilai tugas : ")
uts = input("nilai uts : ")
uas = input("nilai uas : ")

presensi_nilai = float(10/100) * float(presensi)
tugas_nilai = float(20/100) * float(tugas)
uts_nilai = float(30/100) * float(uts)
uas_nilai = float(40/100) * float(uas)

nilai_akhir = float(presensi_nilai + tugas_nilai + uts_nilai + uas_nilai)

if nilai_akhir >= 85:
    grade = "A"
elif nilai_akhir >= 80:
    grade = "A-"
elif nilai_akhir >= 75:
    grade = "B+"
elif nilai_akhir >= 70:
    grade = "B"
elif nilai_akhir >= 60:
    grade = "C"
else:
    grade = "D"

print("\nData Nilai akhir")
print("="*20)
print("nilai presensi : ", presensi)
print("nilai tugas : ", tugas)
print("nilai uts ", uts)
print("nilai uas : ", uas)
print("Nilai akhir : ", nilai_akhir)
print("Grade: ", grade)