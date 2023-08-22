def lonNhat(a):
    tongchan = 0
    tongle = 0
    for max in a:
        if max % 2 == 0:  # Tong Chan
            tongchan += max

        else:
            tongle += max  # Tong le

    return tongchan, tongle


A = [1, 4, 5, 6, 7, 8]
# print("Nhap a: ")
# b = input()
print(("Tong chan,le:"), lonNhat(A))
