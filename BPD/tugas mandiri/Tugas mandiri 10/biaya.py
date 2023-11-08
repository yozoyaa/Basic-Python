def get_biaya(nim):
    kode_ps = nim[2:4]
    biaya_dict = {
        '11': 9800000,
        '12': 8500000,
        '13': 9200000
    }
    return biaya_dict.get(kode_ps, 'Kode program studi tidak diketahui')
