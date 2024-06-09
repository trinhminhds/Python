import random


# def generate_fake_phone_number():
#     # Đầu số điện thoại tùy chọn (ở đây là số 09)
#     area_code = "09"
#     # Tạo 7 chữ số còn lại của số điện thoại
#     number = "".join([str(random.randint(0, 9)) for _ in range(7)])
#     # Ghép đầu số và số còn lại để tạo số điện thoại hoàn chỉnh
#     phone_number = area_code + number
#     return phone_number

#     # Tạo danh sách 2000 số điện thoại ảo


# fake_phone_numbers = [generate_fake_phone_number() for _ in range(3000)]

# # In ra danh sách số điện thoại ảo
# for phone_number in fake_phone_numbers:
#     print(phone_number + ",")


# def generate_fake_phone_number():
#     # Đầu số điện thoại tùy chọn (ở đây là số 09)
#     area_code = "ABC"
#     # Tạo 7 chữ số còn lại của số điện thoại
#     number = "".join(str(random.randint(1, 3000)))
#     # Ghép đầu số và số còn lại để tạo số điện thoại hoàn chỉnh
#     phone_number = area_code + number
#     return phone_number


# Tạo danh sách 2000 số điện thoại ảo
# fake_phone_numbers = [generate_fake_phone_number() for _ in range(3000)]

# In ra danh sách số điện thoại ảo
# for phone_number in fake_phone_numbers:
#     print(phone_number + ",")


# import pandas as pd

# # Đọc hai tập tin CSV
# df1 = pd.read_csv("D:/Downloads/javadatabase (1).csv", dtype=str)
# df2 = pd.read_csv("D:/Downloads/javadatabase.csv", dtype=str)

# # Hợp nhất hai DataFrame lại với nhau bằng cách sử dụng phương thức concat()
# merged_df = pd.concat([df1, df2], ignore_index=True)


# # Lưu DataFrame hợp nhất thành một tập tin CSV mới
# merged_df.to_csv("D:/Downloads/merged_file.csv", index=False)

# print("Hợp nhất hai tập tin CSV thành công!")


# import pandas as pd


# def set_salary_based_on_position(file_path):
#     # Đọc tập tin CSV
#     df = pd.read_csv(file_path, dtype=str)

#     # Kiểm tra điều kiện và cập nhật cột lương
#     df["luong"] = df.apply(
#         lambda row: (
#             40000
#             if row["chucvu"] == "Kỹ sư"
#             else (
#                 50000
#                 if row["chucvu"] == "Chuyên gia nước ngoài"
#                 else (
#                     10000
#                     if row["chucvu"] == "Công nhân"
#                     else (
#                         15000
#                         if row["chucvu"] == "Nhân viên"
#                         else (
#                             8000
#                             if row["chucvu"] == "Thực tập sinh"
#                             else (
#                                 10000
#                                 if row["chucvu"] == "Lao động phổ thông"
#                                 else (
#                                     9000
#                                     if row["chucvu"] == "Người làm bán thời gian"
#                                     else (
#                                         60000
#                                         if row["chucvu"] == "Cán bộ quản lý"
#                                         else (
#                                             9000
#                                             if row["chucvu"] == "Nhân sự thử việc"
#                                             else row["luong"]
#                                         )
#                                     )
#                                 )
#                             )
#                         )
#                     )
#                 )
#             )
#         ),
#         axis=1,
#     )

#     # Lưu DataFrame đã cập nhật lại thành tập tin CSV mới
#     df.to_csv("D:/Downloads/updated_file.csv", index=False)

#     print("Đã cập nhật cột lương dựa trên chức vụ thành công!")


# # Gọi hàm và truyền đường dẫn đến tập tin CSV
# set_salary_based_on_position("D:/Downloads/employee_data.csv")


# import pandas as pd

# # Đọc dữ liệu từ tập tin CSV hoặc bất kỳ nguồn dữ liệu nào khác
# df = pd.read_csv("D:/Downloads/employee_data.csv", dtype=str)

# # Đếm số lượng giá trị duy nhất trong cột "manhanvien"
# # num_unique_values = df["manhanvien"].nunique()

# # Tạo một danh sách các giá trị mới từ "ABC1" đến "ABC2000"
# new_values = ["ABC" + str(i) for i in range(1, 2000)]

# # Tạo một từ điển ánh xạ từ giá trị cũ sang giá trị mới
# value_mapping = dict(zip(df["manhanvien"], new_values))

# # Thay đổi các giá trị trong cột "manhanvien"
# df["manhanvien"] = df["manhanvien"].map(value_mapping)

# # Lưu DataFrame đã thay đổi lại thành tập tin CSV mới nếu cần
# df.to_csv("D:/Downloads/ten_file_moi.csv", index=False)


# import pandas as pd

# # Đọc dữ liệu từ tập tin CSV hoặc bất kỳ nguồn dữ liệu nào khác
# df = pd.read_csv("D:/Downloads/employee_data.csv", dtype=str)

# # Tạo một Series mới chứa các giá trị từ 1 đến 2000
# new_values = pd.Series(range(1, 2001))

# # Gán Series mới này vào cột "manhanvien" của DataFrame
# df["manhanvien"] = new_values

# # Lưu DataFrame đã thay đổi lại thành tập tin CSV mới nếu cần
# df.to_csv("D:/Downloads/ten_file_moi.csv", index=False)


import pandas as pd

list_tenbaocao = [
    "Báo cáo doanh thu",
    "Báo Cáo phản hồi khách hàng",
    "Báo cáo tuyển thêm nhân viên",
    "Báo cáo phân tích cạnh tranh",
    "Báo cáo chất lượng thức ăn",
    "Báo cáo thực đơn",
    "Báo cáo thói quen khách hàng",
    "Báo cáo rủi ro",
    "Báo cáo cơ hội",
    "Báo cáo quảng cáo",
    "Báo cáo tiếp thị",
    "Báo cáo nhu cầu khách hàng",
    "Báo cáo chiến lược",
    "Báo cáo giá cả",
    "Báo cáo hoạt động hành ngày",
    "Báo cáo hoạt động hàng tháng",
    "Báo cáo hoạt động hàng năm",
    "Báo cáo doanh thu quý",
    "Báo cáo phát triển trong tương lai",
    "Báo cáo hiệu suất kinh doanh",
    "Báo cáo hiệu suất làm việc",
]

data = []
for i in range(1, 20):
    data.append(
        [
            "BC" + str(i),
            random.randint(8000, 8651),
            list_tenbaocao[i],
            f"{random.randint(1,30)}/{random.randint(1,12)}/{random.randint(2022,2023)}",
            "NULL",
        ]
    )

df = pd.DataFrame(data, columns=["MABC", "MANV", "TENBC", "NGAYLAP", "NOIDUNG"])


df.to_csv("D:/Downloads/baocao.csv", index=False)
# df.to_csv(duong_dan_file, index=False)

print("File đã được tạo và lưu vào")
