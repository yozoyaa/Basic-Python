def InputData(N):
    data_list = []
    print(f"Masukkan {N} bilangan:")
    for _ in range(N):
        num = int(input("> "))
        data_list.append(num)
    return data_list

def Proses(data_list):
    return [num for num in data_list if num % 2 == 0]

def CetakHasil(hasil):
    print("{:<10} {}".format("No. Indeks", "Bilangan Genap"))
    for idx, num in enumerate(hasil, 1):
        print("{:<10} {}".format(idx, num))

def main():
    N = int(input("Berapa banyak data yang ingin Anda input? "))
    data_list = InputData(N)
    hasil = Proses(data_list)
    CetakHasil(hasil)

if __name__ == "__main__":
    main()
