import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('FoodPrice_in_Turkey.csv')
# print(df)


# vẽ biểu đồ cột so sánh giá gạo tháng 12 năm 2019 của Ankara, Istanbul, Izmir và Nation Average
# data1 = df[(df['Year'] == 2019) & (df['Month'] == 12) & (df['ProductName'] == 'Rice - Retail')]
# # print(data1)
# plt.title("Gia gao thang 12 nam 2019")
# plt.bar(data1['Place'], data1['Price'])
# plt.show()

# Vẽ biểu đồ đường phân tích xu hướng giá gạo (Rice-Retail) trung bình cả nước (National Average) trong năm 2019 tại Thổ Nhĩ Kì
# data2 = df[(df['Place'] == 'National Average') & (df['Year'] == 2019) & (df['ProductName'] == 'Rice - Retail')]
# plt.plot(data2['Month'], data2['Price'])
# plt.show()

# Vẽ biểu đồ Scatter phân tích mối liên quan giữa giá gạo và giá gas trung bình quốc gia (National Average) tại Thổ Nhĩ Kì

x = df[(df['Place'] == 'National Average') & (df['ProductName'] == 'Fuel (gas) - Retail') & (df['Year'] == 2019)]
y = df[(df['Place'] == 'National Average') & (df['ProductName'] == 'Rice - Retail') & (df['Year'] == 2019)]
plt.scatter(x['Price'], y['Price'])
plt.show()
