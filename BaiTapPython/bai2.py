# Nhập độ dài 3 cạnh a, b và c từ bàn phím
a = float(input("Nhập độ dài cạnh a: "))
b = float(input("Nhập độ dài cạnh b: "))
c = float(input("Nhập độ dài cạnh c: "))

# Tính chu vi tam giác
p = (a + b + c) / 2

# Tính diện tích tam giác
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5

# Xuất kết quả
print("Diện tích tam giác có 3 cạnh a = {}, b = {}, c = {} là: {}".format(a, b, c, s))
