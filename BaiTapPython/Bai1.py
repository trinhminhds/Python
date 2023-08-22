# Định nghĩa hàm đếm số lượng phần tử = k trong danh sách
def dem_so_luong(A, k):
    count = 0
    for item in A:
        if item == k:
            count += 1
    return count


# Nhập danh sách A và khóa k từ bàn phím
A = [5, 7, 8, 9, 5, 4, 3, 5]
k = int(input("Nhập giá trị khóa k: "))

# Đếm số lượng phần tử = k trong danh sách A
so_luong = dem_so_luong(A, k)

# Xuất kết quả ra màn hình
print("Số lượng phần tử có giá trị bằng", k, "trong danh sách là:", so_luong)
