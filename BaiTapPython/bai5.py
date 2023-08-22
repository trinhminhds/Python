def nhoNhat(a):
    nho = a[0]
    for min in a:
        if min < nho:
            nho = min

    return nho


def duongNhoNhat(b):
    min = b[0]
    for mins in b:
        if mins > 0:
            min = mins
        elif mins < min:
            min = mins

    return min


A = [-5, -7, -8, -9, -5, -4, -3, -5]
B = [-2, -3, 1]

nho_Nhat = nhoNhat(A)
print("Phan tu nho nhat trong day:", nho_Nhat)


duong_NhoNhat = duongNhoNhat(B)
if duong_NhoNhat > 0:
    print("Phan tu duong nho nhat:", duong_NhoNhat)
else:
    print("Khong co phan tu duong")

nhap = input([])
print(nhap)
