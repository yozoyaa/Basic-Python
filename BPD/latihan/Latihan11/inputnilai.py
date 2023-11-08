from checker import angka
from checker import huruf

def input_nilai():
    data_mahasiswa = {}
    nama_mahasiswa = huruf("Masukan Nama Mahasiswa: ")

    jumlah_tugas = angka("Masukkan jumlah tugas yang diberikan: ")
    nilai_tugas = []
    for i in range(jumlah_tugas):
        nilai = angka(f"Masukkan nilai tugas ke-{i + 1}: ")
        nilai_tugas.append(nilai)

    nilai_uts = angka("Masukan Nilai UTS: ")
    nilai_uas = angka("Masukan Nilai UAS: ")
    nilai_quiz = angka("Masukan Nilai QUIZ: ")

    data_mahasiswa ['nama'] = nama_mahasiswa
    data_mahasiswa ['nilai_tugas'] = nilai_tugas
    data_mahasiswa ['jumlah_tugas'] = jumlah_tugas
    data_mahasiswa ['nilai_uts'] = nilai_uts
    data_mahasiswa ['nilai_uas'] = nilai_uas
    data_mahasiswa ['nilai_quiz'] = nilai_quiz

    return data_mahasiswa
