import pandas as pd
import numpy as np

# Sử dụng pandas để đọc dữ liệu
df = pd.read_csv('OnlineRetail.csv')

# Sử dụng hàm info(), describe() để kiểm tra và mô tả bộ dữ liệu
# print(df.info())
# print(df.describe())

# Sử dụng isNa để tìm dữ liệu khuyết thiếu
print(df.isnull())

# Sử dụng kiến thức bản thân để xác định dữ liệu khuyết thiếu có gây ảnh hưởng
# Sử dụng fillNa để xử lý dữ liệu khuyết thiết
# Giá trị ngoại lai của thuộc tính Quantity chứa giá trị <0, giá trị ngoại lai của UnitPrice =0?