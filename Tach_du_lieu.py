import pandas as pd

df = pd.read_csv('Bai_tap_Thuc_hanh\shopeep_koreantop_clothing_shop_data.csv')
# print(df.head())

df = df[['date_collected','shop_location','response_time']]
# print(df)

# Tách cột shop_location thành 2 cột District và City
df['District']=df['shop_location'].str.split(',').str[0]
df['City']=df['shop_location'].str.split(',').str[1]
# print(df)

# Tách cột date_collected thành 3 cột Day, Month, Year
df['Day']=pd.to_datetime(df['date_collected'],format='%Y-%m-%d').dt.day
df['Month']=pd.to_datetime(df['date_collected'],format='%Y-%m-%d').dt.month
df['Year']=pd.to_datetime(df['date_collected'],format='%Y-%m-%d').dt.year
# print(df)

# Tách cột response_time thành 3 cột Hour, Minute, Second
df['Hour']=pd.to_datetime(df['response_time'],format=' %H:%M:%S').dt.hour
df['Minute']=pd.to_datetime(df['response_time'],format=' %H:%M:%S').dt.minute
df['Second']=pd.to_datetime(df['response_time'],format=' %H:%M:%S').dt.second
print(df)