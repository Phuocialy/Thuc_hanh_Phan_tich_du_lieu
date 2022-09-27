import pandas as pd

df = pd.read_csv('OnlineRetail.csv')
# Đọc bộ dữ liệu, cho biết số dòng, số cột và kiểu dữ liệu của các thuộc tính.
# print(df)
# print(df.info())

# Xây dựng bảng Pivot table, với mỗi Khách hàng cho biết số lượng mua hàng lớn nhất và nhỏ nhất theo Kho. 
#columns là CustomerID vs StockCode
table_1 = df.pivot_table(values='Quantity', index='StockCode', columns='CustomerID', aggfunc='max')
print(table_1)

# Xây dựng bảng Pivot table, với mỗi Số hóa đơn tính trung bình cộng số lượng các mặt hàng theo từng Quốc gia.
data=data[data['Country']=='United Kingdom']
print(data)
data.pivot_table(values=['Quantity'], index=['InvoiceNo','StockCode'], columns='Country', aggfunc ={'Quantity': np.mean})
