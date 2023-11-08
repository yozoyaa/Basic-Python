def input_nilai():
    data_mahasiswa = {}
    nama_mahasiswa = input("Masukan Nama Mahasiswa: ")

    jumlah_tugas = int(input("Masukkan jumlah tugas yang diberikan: "))
    nilai_tugas = []
    for i in range(jumlah_tugas):
        nilai = float(input(f"Masukkan nilai tugas ke-{i + 1}: "))
        nilai_tugas.append(nilai)

    nilai_uts = int(input("Masukan Nilai UTS: "))
    nilai_uas = int(input("Masukan Nilai UAS: "))
    nilai_quiz = int(input("Masukan Nilai QUIZ: "))

    data_mahasiswa ['nama'] = nama_mahasiswa
    data_mahasiswa ['nilai_tugas'] = nilai_tugas
    data_mahasiswa ['jumlah_tugas'] = jumlah_tugas
    data_mahasiswa ['nilai_uts'] = nilai_uts
    data_mahasiswa ['nilai_uas'] = nilai_uas
    data_mahasiswa ['nilai_quiz'] = nilai_quiz

    return data_mahasiswa
