import pandas as pd

# Doc du lieu tu file csv

df = pd.read_csv('FoodPrice_in_Turkey.csv')
print(df)

# Doc du lieu tu file excel

df1 = pd.read_excel('house_price_dong_da.xlsx')
print(df1)

# Doc du lieu tu file json

df2 = pd.read_json('FoodPrice.json')
print(df2)