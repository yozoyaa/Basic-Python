# variable

nama = 'Ahmad Budi'
fakultas = 'FTI'
matakuliah = 'BPD'
nilai_tugas = 65
nilai_uts = 75
nilai_uas = 80
nilai_akhir = int((nilai_tugas + nilai_uts + nilai_uas) / 3)
profil = ('anak ke 2', 165, 60.25)
hobi = ('nonton', 'traveling', 'kuliner')
Kampus = 'Budi Luhur'

#1
print('Data Nilai Mahasiswa BPD')
print('=' * 20)
print('Nama\t\t\t:', nama)
print('Fakultas \t\t:', fakultas)
print('Matakuliah\t\t:', matakuliah)
print('Nilai Tugas\t\t:', nilai_tugas)
print('Nilai UTS\t\t:', nilai_uts)
print('Nila UAS\t\t:', nilai_uas)
print('=' * 20)
print('Nilai akhir\t\t:', nilai_akhir)
print('\n')

#2
print('Profileku')
print('=' * 20)
print('Nama\t\t\t:', nama)
print(type(nama))
print('Fakultas \t\t:', fakultas)
print(type(fakultas))
print('Matakuliah\t\t:', matakuliah)
print(type(matakuliah))
print('Nilai akhir\t\t:', nilai_akhir)
print(type(nilai_akhir))
print('Profil\t\t\t:', profil)
print(type(profil))
print('\n')

#3
print('Profileku')
print('=' * 20)
print('Nama\t\t\t:', nama)
print('Fakultas \t\t:', fakultas)
print('Matakuliah\t\t:', matakuliah)
print('Nilai akhir\t\t:', nilai_akhir)
print('Profil\t\t\t:', profil)
print('Hobi\t\t\t:', hobi)
print('Kampus\t\t\t:', Kampus)
print(f"{'Membandingkan isi variable' : ^50}")
print('nama is kampus\t\t : ', nama is Kampus)
print('profil is not hobi\t : ', profil is not hobi)