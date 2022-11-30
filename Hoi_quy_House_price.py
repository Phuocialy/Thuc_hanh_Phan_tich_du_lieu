# Load in our libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
import os

df = pd.read_csv("AmesHousing.csv")
#Since Regression needs numerical features,convert categorical columns into dummy variables
df1= pd.get_dummies(df)
df1.head()
#Look for columns with any NaN(missing) values
df1.columns[df1.isna().any()].tolist()

#Number of NaN values columnwise
df1.isna().sum()
#Define function to impute series with it's median
def impute_median(series):
    return series.fillna(series.median())
df1['Lot Frontage']= df1['Lot Frontage'].transform(impute_median)
df1['Mas Vnr Area']=df1['Mas Vnr Area'].transform(impute_median)
df1['BsmtFin SF 1']=df1['BsmtFin SF 1'].transform(impute_median)
df1['BsmtFin SF 2']=df1['BsmtFin SF 2'].transform(impute_median)
df1['Bsmt Unf SF']=df1['Bsmt Unf SF'].transform(impute_median)
df1['Total Bsmt SF']=df1['Total Bsmt SF'].transform(impute_median)
df1['Bsmt Full Bath']=df1['Bsmt Full Bath'].transform(impute_median)
df1['Bsmt Half Bath']=df1['Bsmt Half Bath'].transform(impute_median)
df1['Garage Cars']=df1['Garage Cars'].transform(impute_median)
df1['Garage Area']=df1['Garage Area'].transform(impute_median)
#Check remaining columns with NaN values
df1.columns[df1.isna().any()].tolist()
#Define target array y
y= df2['SalePrice'].values

#Create feature array X
X= df2.drop('SalePrice',axis=1).values
#Split the arrays into training and testing data sets
X_train, X_test,y_train, y_test= train_test_split(X,y,test_size=0.3,random_state=42)
#Create a regressor object
LR= LinearRegression()

#Fit training set to the regressor
LR.fit(X_train,y_train)

#print("Mô hình hồi quy tuyến tính đã được huấn luyện, có các tham số:")
#print("Intercept =", LR.intercept_)
#print("Coefficients:", LR.coef_)
