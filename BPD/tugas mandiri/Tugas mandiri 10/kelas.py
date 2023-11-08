def get_kelas(nim):
    kode_kelas = nim[5]
    kelas_dict = {
        '0': 'Regular',
        '1': 'Sore'
    }
    return kelas_dict.get(kode_kelas, 'Kode kelas tidak diketahui')
