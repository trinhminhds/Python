def nhapDay(a):
    lst = []
    n = int(input("Nhập số lượng phần tử của danh sách: "))
    for i in range(n):
        lst.append(int(input("a[{}]= ".format(i))))
    # print("Phần tử dương nhỏ nhất trong danh sách là:", min(filter(lambda x: x > 0, lst)))
    return lst


def nho(c):
    return min([i for i in c[0::1]])


def duongNhoNhat(d):
    return min(filter(lambda x: x > 0, d[0::1]))


def tongViTriChan(b):
    return sum([i for i in b[::2]])


xuatday = nhapDay("a")

print("Phan tu nho nhat:", min(xuatday))

if duongNhoNhat(xuatday) > 0:
    print("Phan tu duong nho nhat:", duongNhoNhat(xuatday))
else:
    print("Khong co phan tu duong")

if tongViTriChan(xuatday):
    print("Tong phan tu duong tai vi tri chan:", tongViTriChan(xuatday))
else:
    print("Khong co phan tu duong")
