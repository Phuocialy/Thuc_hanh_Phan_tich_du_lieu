import pandas as pd
import numpy as np

# Sử dụng pandas để đọc dữ liệu
df = pd.read_csv('house_price_Dống-Da_Hà-Nội_subdata.csv')

# Sử dụng hàm info(), describe() để kiểm tra và mô tả bộ dữ liệu
print(df.info())
print(df.describe())

# Sử dụng isNa để tìm dữ liệu khuyết thiếu
print(df.isnull().sum())
# Sử dụng dropNa để xóa dữ liệu
df = df.dropna()
# Sử dụng fillNa để xử lý dữ liệu khuyết thiết
# Sử dụng các hàm scaling để chuẩn hóa dữ liệu