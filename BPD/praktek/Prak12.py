list1 = []

class Mahasiswa:
    def __init__(self, nama, umur, idnumber):
        self.nama = nama
        self.umur = umur
        self.idnumber = idnumber


class Mhs_Karyawan(Mahasiswa):
    def __init__(self, nama, umur, gaji, idnumber):
        Mahasiswa.__init__(self, nama, umur, idnumber)
        self.gaji = gaji
        self.idnumber = idnumber


    def info(self):
        return self.gaji


class Mhs_Pascaarjana(Mahasiswa):
    def __init__(self, nama, umur, hari, idnumber):
        Mahasiswa.__init__(self, nama, umur, idnumber)
        self.hari = hari
        self.idnumber = idnumber


    def info(self):
        return self.hari


mhs1 = Mhs_Karyawan('budi', 25, 3000000, '1711512020')
mhs2 = Mhs_Pascaarjana('Andi', 40, "Sabtu", '1761180801')
Mahasiswa = [mhs1, mhs2]
for orang in Mahasiswa:
    print(orang.idnumber, orang.nama, orang.umur, orang.info())
