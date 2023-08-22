# gioi han boi cap ngoac vuong []
# cac phan tu cua list cach nhau boi dau ,
# List co kha nang chua moi gia tri doi tuong cua python
# va bao gom chinh no

a = [i for i in range(17)]
print (a)

b = [[n*1,n*2] for n in range(1,3)]
print (b)

# lay gia tri trong chuoi
c = [2,3,'M','i','n','h',[1,7]]
d = c[0:2]
print(d) 
# doi gia tri trong chuoi
c[-1] = 'Ngoc'
print(c)

# Ma tran
p = [[1,2,3],[4,5,6],[7,8,9]]
print (p[0])
print (p[1])
print (p[2])

