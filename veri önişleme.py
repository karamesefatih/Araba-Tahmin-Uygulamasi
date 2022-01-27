# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 18:01:20 2021

@author: CASPER
"""

import pandas as pd

df_2 = pd.read_excel("Dönem_projesi.xlsx")
df_2.drop("Unnamed: 0", axis = 1, inplace = True) 


df_2 = df_2.rename(columns = {"0":"tarih",
                     "1":"marka",
                     "2":"model",
                     "3":"varyant",
                     "4":"model_yılı",
                     "5":"km",
                     "6":"yakıt_türü",
                     "7":"vites",
                     "8":"motor_hacmi",
                     "9":"motor_gücü",
                     "10":"kimden",
                     "11":"fiyat",
                  })


df_2.loc[df_2.kimden == "Sah", "kimden"] = "Sahibinden"
df_2.loc[df_2.kimden == "Gal", "kimden"] = "Galeriden"
df_2["motor_gücü"] = df_2.motor_gücü.str[:-3]







df_3 = pd.read_excel("SON.xlsx")
from sklearn import preprocessing 
le = preprocessing.LabelEncoder()
df_3["Marka"] = le.fit_transform(df_2.marka)
df_3["Model_Yılı"] = le.fit_transform(df_2.model_yılı)
df_3["KM"] = le.fit_transform(df_2.km)
df_3["Yakıt Türü"] = le.fit_transform(df_2.yakıt_türü)
df_3["Vites"] = le.fit_transform(df_2.vites)
df_3["Motor Hacmi"] = le.fit_transform(df_2.motor_hacmi)
df_3["Motor Gücü"] = le.fit_transform(df_2.motor_gücü)
df_3["Kimden"] = le.fit_transform(df_2.kimden)
df_3["Fiyat(Bin)"] = le.fit_transform(df_2.fiyat)
df_3.to_excel("SON2.xlsx")
