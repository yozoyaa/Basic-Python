def huruf(pesan):
    while True:
        try:
            return str(input(pesan))
        except ValueError:
            print("Input yang dimasukan salah! gunakan huruf")


def angka(pesan):
    while True:
        try:
            return int(input(pesan))
        except ValueError:
            print("Input yang dimasukan salah! gunakan angka")


def floats(pesan):
    while True:
        try:
            return float(input(pesan))
        except ValueError:
            print("Input yang dimasukan salah! gunakan angka")


class Customer():
    def __init__(self, idnumber, nama, alamat, telepon):
        self.idnumber = huruf(f"Masukan ID Number Member / NonMember:{idnumber}")
        self.nama = huruf(f"Masukan Nama Member / NonMember:{nama}")
        self.alamat = huruf(f"Masukan Alamat Member / NonMember:{alamat}")
        self.telepon = huruf(f"Masukan No Telpon Member / NonMember:{telepon}")


class Member(Customer):
    def __init__(self, idnumber, nama, alamat, telepon, hargamember, diskon, totalbiaya):
        super().__init__(idnumber, nama, alamat, telepon)
        self.hargamember = angka(f"Masukan Harga Member:{hargamember}")
        self.diskon = floats(f"Masukan Diskon: gunakan decimal:{diskon}")
        self.totalbiaya = totalbiaya


    def tampil_biaya(self):
        self.diskon = self.hargamember * self.diskon
        self.totalbiaya = self.hargamember - self.diskon
        print("Harga Member\t: ", self.hargamember, "\nDiskon\t\t\t: ", self.diskon, "\nTotal Biaya\t\t:", self.totalbiaya)


    def tampil_profil(self):
        print("Id number\t\t:", self.idnumber, "\nNama\t\t\t:", self.nama, "\nlamat\t\t\t:", self.alamat,
              "\nTelepon\t\t\t:", self.telepon)


class Nonmember(Customer):
    def __init__(self, idnumber, nama, alamat, telepon, harganonmember, totalbiaya):
        super().__init__(idnumber, nama, alamat, telepon)
        self.harganonmember = angka(f"Masukan Harga NON Member:{harganonmember}")
        self.totalbiaya = totalbiaya


    def tampil_biaya(self):
        self.totalbiaya = self.harganonmember
        print("Harga non member:", self.harganonmember, "\nTotal Biaya\t\t:", self.totalbiaya)


    def tampil_profil(self):
        print("Id number\t\t:", self.idnumber, "\nNama\t\t\t:", self.nama, "\nlamat\t\t\t:", self.alamat,
              "\nTelepon\t\t\t:", self.telepon)


member1 = Member(idnumber=" ", nama=" ", alamat=" ", telepon=" ", hargamember=" ", diskon=" ", totalbiaya=" ")
nonmember1 = Nonmember(idnumber=" ", nama=" ", alamat=" ", telepon=" ", harganonmember=" ", totalbiaya=" ")
# bisa di tambahin sesuka lo dah nih membernya. misalnya nonmember2 = Nonmember(). jan lupa dimasukin variablenya ke-
# dalam list dibawah ok ok?

member = [member1]
nonmember = [nonmember1]

for orang in member:
    print(f"\n{'DATA MEMBER' : ^40}")
    print("=" * 40)
    orang.tampil_profil()
    print("=" * 40)
    orang.tampil_biaya()

for orang in nonmember:
    print(f"\n{'DATA NONMEMBER' : ^40}")
    print("=" * 40)
    orang.tampil_profil()
    print("=" * 40)
    orang.tampil_biaya()
