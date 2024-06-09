# -*- coding: utf-8 -*-
import random


list_ho = ["Nguyễn", "Trần", "Lê", "Bùi", "Phạm", "Phan", "Trương", "Võ"]
list_tenlot = [
    "Văn",
    "Thị",
    "Minh",
    "Thế",
    "Trung",
    "Nhật",
    "Quang",
    "Mạnh",
    "Hữu",
    "Hoàng",
    "Gia",
    "Hoài",
]

list_ten = [
    "An",
    "Ân",
    "Anh",
    "Ánh",
    "Bình",
    "Bảo",
    "Bạch",
    "Bích",
    "Băng",
    "Cẩm",
    "Châu",
    "Chi",
    "Cường",
    "Danh",
    "Đức",
    "Dung",
    "Duyên",
    "Diễm",
    "Dương",
    "Đại",
    "Đạt",
    "Duy",
    "Giang",
    "Hồng",
    "Hà",
    "Huỳnh",
    "Hậu",
    "Kim",
    "Kiều",
    "Khanh",
    "Khánh",
    "Khải",
    "Khang",
    "Khôi",
    "Linh",
    "Lợi",
    "Long",
    "My",
    "Mỹ",
    "Nhi",
    "Như",
    "Ngọc",
    "Ngân",
    "Nghĩa",
    "Nhã",
    "Oanh",
    "Phúc",
    "Phước",
    "Phú",
    "Phương",
    "Phượng",
    "Sơn",
    "Sang",
    "Sương",
    "Uyên",
    "Vân",
    "Vỹ",
    "Vinh",
    "Vy",
    "Trang",
    "Tiên",
    "Thanh",
    "Thương",
    "Tài",
    "Thắng",
    "Thành",
    "Tấn",
    "Thịnh",
]

list_diachi = [
    "HCM",
    "Long An",
    "Cần Thơ",
    "Vĩnh Long",
    "Trà Vinh",
    "Nam Định",
    "Tây Ninh",
    "Tiền Giang",
    "An Giang",
]


print("\nTạo dữ liệu cho bảng Lớp")
list_malop = [
    "TU22",
    "TU23",
    "TU24",
    "TC23",
    "TC24",
    "PM21",
    "PM22",
    "PM23",
    "PM24",
    "HT22",
    "HT23",
    "HT24",
    "DL24",
    "MT24",
    "VL24",
    "HC24",
    "HD24",
    "NA22",
    "NA23",
    "NA24",
    "HQ23",
    "HQ24",
    "TM24",
    "DT24",
    "MK24",
    "LU24",
    "SP22",
    "SP23",
    "SP24",
    "TO24",
    "TI24",
]

list_mahp = [
    "001",
    "002",
    "003",
    "004",
    "005",
    "006",
    "007",
    "008",
    "009",
    "010",
    "011",
    "012",
    "013",
    "014",
    "015",
    "016",
    "017",
    "018",
    "019",
    "020",
    "021",
    "022",
]

print("\nTạo dữ liệu cho bảng Sinh Viên")

for i in range(8000, 8651):
    ho = random.choice(list_ho)
    tenlot = random.choice(list_tenlot)
    ten = random.choice(list_ten)
    diachi = random.choice(list_diachi)
    malop = random.choice(list_malop)

    if tenlot == "Văn":
        gioitinh = 1
    elif tenlot == "Thị":
        gioitinh = 0
    else:
        gioitinh = random.choice([1, 0])

    if i < 10:
        mssv = "24000" + str(i)
    elif i < 100:
        mssv = "2400" + str(i)
    elif i < 1000:
        mssv = "240" + str(i)

print(
    "('"
    + str(i)
    + "',N'"
    + ho
    + " "
    + tenlot
    + "',N'"
    + ten
    + "','"
    + str(random.randint(1, 30))
    + "/"
    + str(random.randint(1, 12))
    + "/"
    + str(random.randint(2000, 2005))
    + "',N'"
    + gioitinh
    + "',N'"
    + diachi
    + "','"
    + malop
    + "'),"
)

print(
    str(i)
    + ","
    + ho
    + " "
    + tenlot
    + ","
    + ten
    + ","
    + str(random.randint(2000, 2005))
    + "-"
    + str(random.randint(1, 12))
    + "-"
    + str(random.randint(1, 30))
    + ","
    + str(gioitinh)
    + ","
    + diachi
    + ","
    + malop
)


f = open("/Users/tranthuan/Desktop/rs.csv", "a")
for i in range(2416, 8651):
    list_mahp = [
        "001",
        "002",
        "003",
        "004",
        "005",
        "006",
        "007",
        "008",
        "009",
        "010",
        "011",
        "012",
        "013",
        "014",
        "015",
        "016",
        "017",
        "018",
        "019",
        "020",
        "021",
        "022",
    ]
    for j in range(1, random.randint(3, 7)):
        mahp = random.choice(list_mahp)
        diem = random.uniform(4, 10)
        list_mahp.remove(mahp)
        f.write(str(i) + "," + mahp + "," + str(round(diem, 1)) + "\n")


f.close()
