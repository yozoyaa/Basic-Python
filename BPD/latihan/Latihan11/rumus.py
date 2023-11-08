def hitung_nilai_akhir(data_mahasiswa):
    rata_rata_tugas = sum(data_mahasiswa['nilai_tugas']) / len(data_mahasiswa['nilai_tugas'])
    nilai_akhir = (
        rata_rata_tugas * 0.3 +
        data_mahasiswa['nilai_uts'] * 0.35 +
        data_mahasiswa['nilai_uas'] * 0.25 +
        data_mahasiswa['nilai_quiz'] * 0.1
    )
    return nilai_akhir
