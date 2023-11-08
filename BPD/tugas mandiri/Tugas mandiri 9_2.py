def sum_lists(list_a, list_b):
    if len(list_a) != len(list_b):
        print("List tidak memiliki jumlah elemen yang sama!")
        return None

    sum_list = [a + b for a, b in zip(list_a, list_b)]
    return sum_list


list_a = [1, 2, 4, 8]
list_b = [16, 32, 64, 128]

result = sum_lists(list_a, list_b)
print("Hasil penjumlahan list A dan B adalah:", result)

