a = "Trinh Ngoc Minh 5"
b = a.count('i')
print(b)
# count(m, bat dau , ket thuc) = dem so lan xuat hien cua m trong chuoi

# startswith(m, bat dau, ket thuc) = bao m co phai ky tu dau tien trong chuoi hay khong (dung, sai)
r = a.startswith('T',0,13)
print(r)

# endswith(m,bat dau, ket thuc) = bao co m trong chuoi hay khong (dung , sai)
t = a.endswith('T')
print (t)

# find(m) = bao m xuat hien o vi tri thu may trong chuoi
y = a.find('i')
print (y)

# isdigit() = kiem tra co So(5) trong ky tu khong (dung, sai)
k = '2309'
f = k.isdigit ()
print(f)

# islower() = kiem tra chuoi co chu viet Thuong(minh) het ca chuoi (dung, sai)
g = a.islower()
print(g)

# isupper() = kiem tra chuoi co chu viet Hoa(MINH) het ca chuoi (dung, sai)
v = a.isupper()
print(v)
# isspace() = kiem tra co khoang cach(' ') hay khong (dung, sai)
c = a.isspace()
print(c)