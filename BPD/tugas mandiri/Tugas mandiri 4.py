# Mendefinisikan data mahasiswa dalam list of tuples
students = [
    (1, "Bambang", "081230305656"),
    (2, "Richard", "087123455777"),
    (3, "Budi Tomo", "087809298787"),
    (4, "Kelvin", "085678787878"),
    (5, "Melianda", "021393900097")
]

# Menambahkan data mahasiswa baru ke dalam dictionary
student_dict = {
    6: {"Nama": "Bambang", "Telepon": "081230305656"},
    7: {"Nama": "Richard", "Telepon": "087123455777"}
}

# Mencetak header tabel
print("ID \t Nama Mahasiswa \t Telepon")

# Mencetak data mahasiswa dari list of tuples
for student in students:
    print(student[0], '\t', student[1], '\t\t\t', student[2])

# Mencetak data mahasiswa dari dictionary
for nim, data in student_dict.items():
    print(nim, '\t', data["Nama"], '\t\t\t', data["Telepon"])
