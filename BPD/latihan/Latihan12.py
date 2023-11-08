class Pegawai():
    def __init__(self, idnumber, nama, telepon, department):
        self.idnumber = idnumber
        self.nama = nama
        self.telepon = telepon
        self.department = department


class Pegawai_Tetap(Pegawai):
    def __init__(self, idnumber, nama, telepon, department, gaji_pokok, uang_makan, uangtransport):
        super().__init__(idnumber, nama, telepon, department)
        self.gajipokok = gaji_pokok
        self.uangmakan = uang_makan
        self.uangtransport = uangtransport


    def tampil_gaji(self):
        print("Gaji: ", self.gajipokok, "\nUang Makan: ", self.uangmakan, "\nUang transport: ", self.uangtransport)


    def tampil_info(self):
        return print("\nIdNumber: ", self.idnumber, "\nNama: ", self.nama, "\nTelepon: ", self.telepon, "\nDepartment: ",
              self.department)


class Pegawai_Honorer(Pegawai):
    def __init__(self, idnumber, nama, telepon, department, honor):
        super().__init__(idnumber, nama, telepon, department)
        self.honor = honor


    def tampil_incentif(self):
        return print("Gaji Honor: ", self.honor)


    def tampil_info(self):
        return print("\nIdNumber: ", self.idnumber, "\nNama: ", self.nama, "\nTelepon: ", self.telepon, "\nDepartment: ",
              self.department)


pgw1 = Pegawai_Tetap("2311500967", "Fickry Imamsyah", "082213953988", "Butcher",
                     "20000000", "50000", "25000")
pgw2 = Pegawai_Honorer("235009843", "Arkana Prahasta", "08321862123", "Marketing",
                       "5000000")

pegawai_tetap = [pgw1]
pegawai_honor = [pgw2]

for orang in pegawai_tetap:
    orang.tampil_info(), orang.tampil_gaji()

for orang in pegawai_honor:
    orang.tampil_info(), orang.tampil_incentif()
