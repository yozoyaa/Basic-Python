def get_jurusan(nim):
    kode_ps = nim[2:4]
    jurusan_dict = {
        '11': 'Teknik Informatika',
        '12': 'Sistem Informasi',
        '13': 'Sistem Komputer'
    }
    return jurusan_dict.get(kode_ps, 'Kode program studi tidak diketahui')