class Customer():
    def __init__(self, idnumber, nama, alamat, telepon):
        self.idnumber = idnumber
        self.nama = nama
        self.alamat = alamat
        self.telepon = telepon


class Member(Customer):
    def __init__(self, idnumber, nama, alamat, telepon, hargamember, diskon, totalbiaya):
        super().__init__(idnumber, nama, alamat, telepon)
        self.hargamember = hargamember
        self.diskon = diskon
        self.totalbiaya = totalbiaya


    def tampil_biaya(self):
        self.diskon = self.hargamember * self.diskon
        self.totalbiaya = self.hargamember - self.diskon
        print("Harga Member: ", self.hargamember, "\nDiskon: ", self.diskon, "\nTotal Biaya:", self.totalbiaya)


    def tampil_profil(self):
        print("\nIdnumber:", self.idnumber, "\nNama:", self.nama, "\nAlamat:", self.alamat, "\nTelepon", self.telepon)


class Nonmember(Customer):
    def __init__(self, idnumber, nama, alamat, telepon, harganonmember, totalbiaya):
        super().__init__(idnumber, nama, alamat, telepon)
        self.harganonmember = harganonmember
        self.totalbiaya = totalbiaya


    def tampil_biaya(self):
        self.totalbiaya = self.harganonmember
        print("Harga non member:", self.harganonmember, "\nTotal Biaya:", self.totalbiaya)


    def tampil_profil(self):
        print("\nIdnumber:", self.idnumber, "\nNama:", self.nama, "\nAlamat:", self.alamat, "\nTelepon", self.telepon)


member1 = Member("2311500967", "Fickry Imamsyah", "Jl.Panjang", "082213953988",
                 200000, 0.5, totalbiaya=" ")
member2 = Nonmember("23546422", "Fickry Imamsyah", "Jl.Panjang", "0822134654",
                    300000, totalbiaya=" ")

member = [member1]
nonmember = [member2]

for orang in member:
    orang.tampil_profil(), orang.tampil_biaya()

for orang in nonmember:
    orang.tampil_profil(), orang.tampil_biaya()
