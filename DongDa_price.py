import pandas as pd
import numpy as np

#1. Đọc bộ dữ liệu, cho biết số dòng, số cột và kiểu dữ liệu của các thuộc tính.
df = pd.read_csv('house_price_Dống-Da_Hà-Nội_subdata.csv')
print(df.info())

#2. Lọc ra các bản ghi bán nhà riêng tại phường Trung liệt hoặc phường Khâm Thiên
df1 = df[df['ward_name'] == 'Trung Liệt' ]

#3. Lọc các thông tin Địa chỉ, Giá, Hướng nhà, Hướng ban công của các bản ghi có giấy chứng nhận sổ đỏ và có 3 phòng ngủ trở lên.
df2 = df[['Address', 'Price', 'house_direction', 'balcony_direction', 'land_certificate', 'bedroom']]
df2 = df2[(df2['land_certificate' == 'sổ đỏ']) & df2['bedroom'] >= 3]

#4. Với mỗi loại nhà đất, tính trung bình cộng giá cũng như giá lớn nhất và giá nhỏ nhất.
#5. Tính trung bình cộng số phòng ngủ, số phòng vệ sinh, số tầng của mỗi phường.