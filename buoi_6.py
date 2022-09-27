import pandas as pd

df = pd.read_csv("GDPlist.csv", engine='python')

print(df.dtypes)

# Tính giá trị lớn nhất và nhỏ nhất của GDP.
min_GDP = df['GDP (millions of US$)'].min()
max_GDP = df['GDP (millions of US$)'].max()

# print(min_GDP)
# print(max_GDP)

# Hãy cho biết xu hướng phân bố dữ liệu của GDP.

df_mean = df['GDP (millions of US$)'].mean()
df_median = df['GDP (millions of US$)'].median()
df_mode = df['GDP (millions of US$)'].mode()
# print(df_mean)
# print(df_median)
# print("***")
# print(df_mode)

df_1 = df.groupby('Continent')['GDP (millions of US$)'].agg(['mean', 'median'])
print(df_1)

# mean > median