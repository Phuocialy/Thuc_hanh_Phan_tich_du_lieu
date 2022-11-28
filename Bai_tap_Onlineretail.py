import pandas as pd
import numpy as np

#1. Đọc bộ dữ liệu, cho biết số dòng, số cột và kiểu dữ liệu của các thuộc tính.
df = pd.read_csv('OnlineRetail.csv')
# print(df.info())

#2. Trích xuất dữ liệu các cột Description và Quantity lưu vào file OnlineRetail.csv
df2 = df[['Description', 'Quantity']]
# print(df2.head())
# df2.to_csv('OnlineRetail.csv')

#3. Trích xuất dữ liệu 1000 dòng đầu tiên lưu vào file OnlineRetail.xlsx
df3 = df.head(1000)
# print(df3)
# df3.to_excel('OnlineRetail.xlsx')

#4. Trích xuất dữ liệu các phần tử từ dòng 1000 đến dòng 2000, các cột Quantity, InvoiceDate, UnitPrice lưu vào file OnlineRetail.json
df4 = pd.DataFrame(df, index=range(1000,2001), columns=['Quantity', 'InvoiceDate', 'UnitPrice'])
print(df4)