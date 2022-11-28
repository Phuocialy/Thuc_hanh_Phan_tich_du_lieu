import pandas as pd
import numpy as np

#1.Đọc bộ dữ liệu, cho biết số dòng, số cột và kiểu dữ liệu của các thuộc tính.
df = pd.read_csv('GDPlist.csv', engine='python')
# print(df.info())

#2.Việt hóa tên các cột trong bảng dữ liệu: Country 🡪 Nuoc; Continent 🡪 Chauluc; GDP (millions of US$) 🡪 GDP (trieu $)
df.rename(columns={"Country": "Nuoc"}, inplace=True)
df.rename(columns={"Continent": "Chauluc"}, inplace=True)
df.rename(columns={"GDP (millions of US$)": "GDP (trieu $)"}, inplace=True)
# print(df.info())

#3.Chèn thêm một cột “Thanhpho” vào sau cột “Nuoc”, giá trị ban đầu là giá trị của cột “Nuoc” 
df.insert(
    loc=1,
    column='Thanhpho',
    value=df['Nuoc']
)
# print(df.head())

#4. Trong cột Thanhpho, thay giá trị Vietnam thành Hanoi; Làm tương tự với các nước còn lại.
df['Thanhpho'] = df['Thanhpho'].map({'Vietnam':'Hanoi'})
# print(df.head())

#5. Xóa các bản ghi có Chauluc là ‘Asia’
df.drop(df[df['Chauluc'] == 'Asia'].index, inplace = True)
print(df.head())
 
#6. Xóa các bản ghi có GDP < 300000
df = df.loc[df["GDP (trieu $)"] > 300000 ]
print(df)

