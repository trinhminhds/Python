def nhapDay(a):
    n = int(input("Nhập số phần tử của dãy số : "))
    mylist = []
    for i in range(n):
        nhap = int(input("a[" + str(i) + "]= "))
        mylist.append(nhap)
    return mylist


def nhoNhat(b):
    nho = b[0]
    for min in b:
        if min < nho:
            nho = min

    return nho


def duongNhoNhat(c):
    min = c[0]
    for mins in c:
        if mins > 0:
            continue
        elif mins < min:
            min = mins

    return min


def tongViTriChan(d):
    tong = 0
    viTri = d[0]
    for i in d:
        if i > 0 and viTri % 2 == 0:
            tong += i

    return tong


nhapday = nhapDay("a")
print("Phan tu nho nhat trong day:", nhoNhat(nhapday))

if duongNhoNhat(nhapday) > 0:
    print("Phan tu duong nho nhat:", duongNhoNhat(nhapday))
else:
    print("Khong co phan tu duong")

print("Tong phan tu tai vi tri chan:", tongViTriChan(nhapday))
