def nhapMaTran(a):
    matrix = []
    m = int(input("Nhap so hang cua ma tran: "))
    n = int(input("Nhap so cot cua ma tran: "))
    for i in range(m):
        row = []
        for j in range(n):
            element = int(input(f"Nhập phần tử [{i}][{j}]: "))

            row.append(element)
        matrix.append(row)

    return matrix


def dem(b):
    count = 0
    for row in b:
        for i in row:
            if i > 0 and i % 2 == 0:
                count += 1

    return count


def nhoNhat(c):
    return min([i for i in c[0::1]])


def duongNhoNhat(d):
    duongNho = float("inf")
    for row in d[0::1]:
        for min in row:
            if min > 0 and min < duongNho:
                duongNho = min

        return duongNho


xuatMaTran = nhapMaTran("a")
print("\nMa tran vua nhap:", xuatMaTran)
print("Dem phan tu duong chan:", dem(xuatMaTran))
print("Phan tu nho nhat:", min(nhoNhat(xuatMaTran)))

if duongNhoNhat(xuatMaTran) == float("inf"):
    print("Khong co phan tu duong")
else:
    print("Phan tu duong nho nhat:", duongNhoNhat(xuatMaTran))
