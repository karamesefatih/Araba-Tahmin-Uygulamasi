# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 17:24:50 2021

@author: CASPER
"""

    
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_excel("Dönem_projesi.xlsx")
df.drop("Unnamed: 0", axis = 1, inplace = True) 
print(df.describe())

print("\n**********************************************\n")
print(df.info())

print("\n**********************************************\n")
print("MARKA")
print(df.marka.value_counts())
fig = plt.figure(figsize=(20,5))
df.marka.value_counts().plot(kind = 'pie',autopct='%.1f%%')
plt.ylabel("", fontsize = 20)
plt.title("MARKA");
print("\n**********************************************\n")
print("MODEL")

print(df.model.value_counts())

fig = plt.figure(figsize=(20,5))
df.model.value_counts().plot(kind = 'pie',autopct='%.1f%%')
plt.ylabel("", fontsize = 20)
plt.title("MODEL");
print("\n**********************************************\n")
print("VARYANT")

print(df.varyant.value_counts())
fig = plt.figure(figsize=(20,5))
df.varyant.value_counts().plot(kind = 'pie',autopct='%.1f%%')
plt.ylabel("", fontsize = 20)
plt.title("VARYANT");
print("\n**********************************************\n")
print("")

print(df.model_yılı.value_counts())

fig = plt.figure(figsize=(20,5))
df.model_yılı.value_counts().plot(kind = 'pie',autopct='%.1f%%')
plt.ylabel("", fontsize = 20)
plt.title("MODEL_YILI");
print("\n**********************************************\n")
print("KM")

print(df.km.value_counts())

fig = plt.figure(figsize=(20,5))
df.km.value_counts().plot(kind = 'pie',autopct='%.1f%%')
plt.ylabel("", fontsize = 20)
plt.title("KM");
print("\n**********************************************\n")
print("YAKIT TÜRÜ")

print(df.yakıt_türü.value_counts())
fig = plt.figure(figsize=(20,5))
df.yakıt_türü.value_counts().plot(kind = 'pie',autopct='%.1f%%')
plt.ylabel("", fontsize = 20)
plt.title("YAKIT TÜRÜ");
print("\n**********************************************\n")
print("VİTES")

print(df.vites.value_counts())
fig = plt.figure(figsize=(20,5))

df.vites.value_counts().plot(kind = 'pie',autopct='%.1f%%')
plt.ylabel("", fontsize = 20)
plt.title("VİTES");
print("\n**********************************************\n")
print("MOTOR HACMİ")

print(df.motor_hacmi.value_counts() )

fig = plt.figure(figsize=(20,5))
df.motor_hacmi.value_counts().plot(kind = 'pie',autopct='%.1f%%')
plt.ylabel("", fontsize = 20)
plt.title("MOTOR HACMİ");
print("\n**********************************************\n")
print("MOTOR GÜCÜ")

print(df.motor_gücü.value_counts())

fig = plt.figure(figsize=(20,5))
df.motor_gücü.value_counts().plot(kind = 'pie',autopct='%.1f%%')
plt.ylabel("", fontsize = 20)
plt.title("MOTOR GÜCÜ");
print("\n**********************************************\n")
print("KİMDEN")

print(df.kimden.value_counts())

fig = plt.figure(figsize=(20,5))
df.kimden.value_counts().plot(kind = 'pie',autopct='%.1f%%')
plt.ylabel("", fontsize = 20)
plt.title("kimden");
print("\n**********************************************\n")














































































































































































































































































































































































































































