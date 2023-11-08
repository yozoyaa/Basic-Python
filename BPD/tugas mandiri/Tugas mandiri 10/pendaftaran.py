from kelas import get_kelas
from jurusan import get_jurusan
from biaya import get_biaya

mahasiswa_data = {}
def tambah_mahasiswa(nim, nama, no_hp, email, alamat, nem):
    mahasiswa_data[nim] = {
        'Nama Lengkap': nama,
        'No HP': no_hp,
        'Email': email,
        'Alamat': alamat,
        'NEM': nem,
        'Jurusan': get_jurusan(nim),
        'Kelas': get_kelas(nim),
        'Biaya Kuliah': get_biaya(nim)
    }


def cetak_mahasiswa():
    for nim, info in mahasiswa_data.items():
        print(f"{'DATA MAHASISWA BARU': ^50}")
        print("="*50)
        print(f"NIM\t\t\t\t: {nim}")
        print(f"Nama Lengkap\t: {info['Nama Lengkap']}")
        print(f"No. HP\t\t\t: {info['No HP']}")
        print(f"Email\t\t\t: {info['Email']}")
        print(f"Alamat\t\t\t: {info['Alamat']}")
        print(f"NEM\t\t\t\t: {info['NEM']}")
        print(f"Jurusan\t\t\t: {info['Jurusan']}")
        print(f"Kelas\t\t\t: {info['Kelas']}")
        print(f"Biaya Kuliah\t: {info['Biaya Kuliah']}")
        print("="*50)