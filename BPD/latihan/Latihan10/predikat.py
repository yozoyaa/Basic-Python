def get_predikat(grade):
    predikat = {
        'A': 'Sangat Baik',
        'B': 'Baik',
        'C': 'Cukup',
        'D': 'Kurang',
        'E': 'Gagal'
    }
    return predikat.get(grade, 'Tidak Diketahui')
