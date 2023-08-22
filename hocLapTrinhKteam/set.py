set_1 = {(1, 2, ("Trinh Ngoc Minh"), (17))}
print(set_1)

# Bai tap cung co da khac phuc duoc
set2 = {1, 7}
set3 = set2.copy()
set3.clear()
print(set2)

# Toan tu set
set5 = {1, 2, 3}
set6 = {2, 3}
# Toan tu tru {1}
tru = set5 - set6
print(tru)

# Toan tu lay gia tri giong nhau
trungNhau = set5 & set6
print(trungNhau)

# Toan tu ket hop tat ca gia tri 2set (chi lay 1 gia tri trung nhau)
ketHop = set5 | set6
print(ketHop)

# Toan tu ket hop khong lay gia tri trung nhau
khongTrungNhau = set5 ^ set6
print(khongTrungNhau)
