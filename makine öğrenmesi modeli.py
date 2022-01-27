# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 18:01:37 2021

@author: CASPER
"""


import pandas as pd
import xgboost as xgb
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split, GridSearchCV,cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
from sklearn import model_selection


df_2 = pd.read_excel(r"SON.xlsx")
df_2.drop("Unnamed: 0", axis = 1, inplace = True)
df = df_2.copy()

df.columns 
df = df[["Marka","Model_Yılı","KM","Yakıt Türü","Vites",
         "Motor Hacmi","Motor Gücü","Kimden","Fiyat(Bin)"]]


X = df.drop(["Fiyat(Bin)"], axis = 1)
y = df["Fiyat(Bin)"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 144)
# GridSearchCV
params = {"colsample_bytree":[0.4,0.5,0.6],
         "learning_rate":[0.01,0.02,0.09],
         "max_depth":[2,3,4,5,6],
         "n_estimators":[100,200,500,2000]}
xgb = XGBRegressor()

grid = GridSearchCV(xgb, params, cv = 10, n_jobs = -1, verbose = 2)

grid.fit(X_train, y_train)

df11=grid.best_params_
xgb1 = XGBRegressor(colsample_bytree = 0.6, learning_rate = 0.02, max_depth = 6, n_estimators = 200)

model_xgb = xgb1.fit(X_train, y_train)

model_xgb.predict(X_test)[0:5]
print(X_test)
print(y_test)

model_xgb.score(X_test, y_test)
model_xgb.score(X_train, y_train)
df_7=np.sqrt(-1*(cross_val_score(model_xgb, X_test, y_test, cv=10, scoring='neg_mean_squared_error'))).mean()

df_5=model_xgb.score(X_test, y_test)
df_6=model_xgb.score(X_train, y_train)
importance = pd.DataFrame({"Importance": model_xgb.feature_importances_},
                         index=X_train.columns)









