a = [1, 2, 3]
print(a)
# Ham a.count(1) dem so lan xuat hien cua 1
b = a.count(1)
print(b)

# a.index(2) tim vi tri cua 2
c = a.index(2)
print(c)

# append(9),([9,10]) them 9 vao phan tu list [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,[9,10]]
a.append(4)
print(a)

# extend(a[9,10]) them tung phan tu trong list [1,2,3,4,5,6,7,8,9,10]
a.extend([5, 6])
print(a)

# insert(0,9) them phan tu 9 vao vi tri 0
a.insert(6, 7)
print(a)

# pop(1) lay gia tri 2 cua vi tri 1 ra ngoai
p = a.pop(5)
print(p)

# remove(1) xoa gia tri 1 trong list
a.remove(7)
print(a)

# reverse() dao nguoc chuoi list
a.reverse()
print(a)

# sort(reverse = false, true) sap xep tang dan hoac giam dan
a.sort(reverse=False)
print(a)
