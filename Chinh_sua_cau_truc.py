import pandas as pd

df = pd.read_csv('FoodPrice_in_Turkey.csv')
# print(df.head())

# Doi ten cot thuoc tinh
df.rename(columns={'Place':'Địa điểm','ProductName':'Tên SP'},inplace=True)
# print(df.head())

# Them cot moi voi tat ca gia tri rong NaN
df['new_column'] = 'NaN'
# print(df.head())

# Them cot giam gia 10% cho tat ca cac ban ghi
df['Giảm giá']= pd.Series('10%', index=df.index)
# print(df)

# Them cot moi vao DataFrame
df=df.append({'Địa điểm':'NA','ProductId':'RR','Tên SP':'Rice','UmId':10,'UmName':'KG','Month':6,'Year':2021,'Price':84.3785,'Giảm giá':'10%','Giảm giá 2':'12%'},ignore_index=True)
# print(df.tail())

# Xoa mot cot trong DataFrame
del df['new_column']
# print(df.head())

# Xoa cac dong trong DataFrame
df.drop(2, axis = 0, inplace=True)
print(df.head())