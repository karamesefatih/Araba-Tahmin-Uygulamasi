# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 21:10:11 2021

@author: CASPER
"""


from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import Canvas
from tkinter import ttk
import pandas as pd

df_2 = pd.read_excel(r"SON.xlsx")

df = df_2.copy()
df = df[["Marka","Model_Yılı","KM","Yakıt Türü","Vites",
         "Motor Hacmi","Motor Gücü","Kimden","Fiyat(Bin)"]]
X = df.drop(["Fiyat(Bin)"], axis = 1)
y = df["Fiyat(Bin)"]
from sklearn.model_selection import train_test_split, GridSearchCV,cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import random
import pandas as pd
from sklearn import model_selection
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 144)
import xgboost as xgb
from xgboost import XGBRegressor
xgb1 = XGBRegressor(colsample_bytree = 0.5, learning_rate = 0.09, max_depth = 4, n_estimators = 2000)
model_xgb = xgb1.fit(X_train, y_train)
model_xgb.predict(X_test)[15:20]
model_xgb.score(X_test, y_test)





pencere = Tk()
pencere.title("ARABA FİYAT TAHMİNİ")

pencere.configure(background='#CC0000')
pencere.geometry("1700x900")
pencere.state("normal")




def olumsuz():
    messagebox.showwarning(title="Dikkat", message="Seçim Yapmadınız")

# DEĞİŞKENLER

def marka_düzenle():
    global marka
    marka_deger = marka_kutu.get()
    
       
    if(marka_deger == "Renault"):
        marka = 1
        mesaj()
    elif(marka_deger == "Volkswagen"):
        marka = 2
        mesaj()
    elif(marka_deger == "Ford"):
        marka = 3
        mesaj()
    elif(marka_deger == "Hyundai"):
        marka = 4
        mesaj()
    elif(marka_deger == "Peugeot"):
        marka = 5
        mesaj()
    elif(marka_deger == "Fiat"):
        marka = 6
        mesaj()
    elif(marka_deger == "Mercedes"):
        marka = 7
        mesaj()
    elif(marka_deger == "Tofaş"):
        marka = 8
        mesaj()
    elif(marka_deger == "Toyota"):
        marka = 9
        mesaj()
    elif(marka_deger == "Opel"):
        marka = 10
        mesaj()
    elif(marka_deger == "Dacia"):
        marka = 11
        mesaj()
    elif(marka_deger == "Honda"):
        marka = 12
        mesaj()    
    elif(marka_deger == "Chevrolet"):
        marka = 13
        mesaj()
    elif(marka_deger == "BMW"):
        marka = 14
        mesaj()
    elif(marka_deger == "Audi"):
        marka = 15
        mesaj()
    elif(marka_deger == "Nissan"):
        marka = 16
        mesaj()
    elif(marka_deger == "mini"):
        marka = 17
        mesaj()
    elif(marka_deger == "Mini"):
        marka = 18
        mesaj()    
    elif(marka_deger == "Seat"):
        marka = 19
        mesaj()
    elif(marka_deger == "Land Rover"):
        marka = 20
        mesaj()
    elif(marka_deger == "Citroen"):
        marka = 21
        mesaj()
    elif(marka_deger == "Volvo"):
        marka = 22
        mesaj()
    elif(marka_deger == "Mitsubishi"):
        marka = 23
        mesaj()
    elif(marka_deger == "Jaguar"):
        marka = 24
        mesaj()
    elif(marka_deger == "skoda"):
        marka = 25
        mesaj()
    elif(marka_deger == "Lada"):
        marka = 26
        mesaj()
    elif(marka_deger == "Subaru"):
        marka = 27
        mesaj()
    elif(marka_deger == "Jeep"):
        marka = 28
        mesaj()
    elif(marka_deger == "Alfa Romeo"):
        marka = 29
        mesaj()
    elif(marka_deger == "Dodge"):
        marka = 30
        mesaj()
    elif(marka_deger == "Tata"):
        marka = 31
        mesaj()
    elif(marka_deger == "Chrysler"):
        marka = 32

  
    else:
        olumsuz()
    print(marka)
        
    
        
    
def yıl_düzenle():
    global yıl
    yıl_deger = yıl_kutu.get()
    if(yıl_deger == "2015"):
        yıl = 0
        mesaj()
    elif(yıl_deger == "2017"):
        yıl = 1
        mesaj()
    elif(yıl_deger == "2012"):
        yıl = 2
        mesaj()   
    elif(yıl_deger == "2013"):
        yıl = 3
        mesaj()   
    elif(yıl_deger == "2011"):
        yıl = 4
        mesaj()  
    elif(yıl_deger == "2016"):
        yıl = 5
        mesaj() 
    elif(yıl_deger == "2014"):
        yıl = 6
        mesaj()  
    elif(yıl_deger == "2005"):
        yıl = 7
        mesaj()
    elif(yıl_deger == "2004"):
        yıl = 8
        mesaj()
    elif(yıl_deger == "2020"):
        yıl = 9
        mesaj()   
    elif(yıl_deger == "2007"):
        yıl = 10
        mesaj()   
    elif(yıl_deger == "2019"):
        yıl = 11
        mesaj()  
    elif(yıl_deger == "2010"):
        yıl = 12
        mesaj() 
    elif(yıl_deger == "2001"):
        yıl = 13
        mesaj()  
    elif(yıl_deger == "1996"):
        yıl = 14
        mesaj()  
    elif(yıl_deger == "2008"):
        yıl = 15
        mesaj()
    elif(yıl_deger == "2000"):
        yıl = 16
        mesaj()   
    elif(yıl_deger == "1997"):
        yıl = 17
        mesaj()   
    elif(yıl_deger == "2009"):
        yıl = 18
        mesaj()  
    elif(yıl_deger == "2006"):
        yıl = 19
        mesaj() 
    elif(yıl_deger == "1998"):
        yıl = 20
        mesaj()  
    elif(yıl_deger == "2018"):
        yıl = 21
        mesaj()
    elif(yıl_deger == "2010"):
        yıl = 22
        mesaj() 
    elif(yıl_deger == "1994"):
        yıl = 23
        mesaj()  
    elif(yıl_deger == "1957"):
        yıl = 24
        mesaj()  
    elif(yıl_deger == "1977"):
        yıl = 25
        mesaj()
    elif(yıl_deger == "1991"):
        yıl = 26
        mesaj()   
    elif(yıl_deger == "1987"):
        yıl = 27
        mesaj()   
    elif(yıl_deger == "2003"):
        yıl = 28
        mesaj()  
    elif(yıl_deger == "2002"):
        yıl = 29
        mesaj() 
    elif(yıl_deger == "1999"):
        yıl = 30
        mesaj()  
    elif(yıl_deger == "1995"):
        yıl = 31
        mesaj()
    elif(yıl_deger == "2021"):
        yıl = 32
 
    else:
        olumsuz()
        
def km_düzenle():
    global km
    km_araç = int(km_entry.get())
    if(km_araç > 0):
        km = km_araç
      
        print(km_araç)
    else:
        olumsuz()

    
def yakıt_düzenle():
    global yakıt
    yakıt_deger = yakıt_kutu.get()
    if(yakıt_deger == "Dizel"):
        yakıt = 0
        mesaj()
    elif(yakıt_deger == "Benzin/LPG"):
        yakıt = 1
        mesaj()
    elif(yakıt_deger == "Benzin"):
        yakıt = 2
        mesaj()
    elif(yakıt_deger == "Hibrit"):
        yakıt = 3
        mesaj()
    elif(yakıt_deger == "Elektrik"):
        yakıt = 4
      
    else:
        olumsuz()
       
        
       
        
def vites_düzenle():
    global vites
    vites_deger = vites_kutu.get()
    if(vites_deger == "Düz Vites"):
        vites = 0
        mesaj()
    elif(vites_deger == "Otomatik Vites"):
        vites = 1
        mesaj()
    elif(vites_deger == "Yarı Otomatik Vites"):
        vites = 2
  
    else:
        olumsuz()

    
def hacim_düzenle():
    global hacim
    hacim_deger = hacim_kutu.get()
    if(hacim_deger == "1301-1600 cc"):
        hacim = 0
        mesaj()
    elif(hacim_deger == "1300 cc ve altı"):
        hacim = 1
        mesaj()
    elif(hacim_deger == "1801-2000 cc"):
        hacim = 2
        mesaj()
    elif(hacim_deger == "1601-1800 cc"):
        hacim = 3
        mesaj()
    elif(hacim_deger == "Bilinmiyor"):
        hacim = 4
        mesaj()
    elif(hacim_deger == "2501-3000 cc"):
        hacim = 5
        mesaj()
    elif(hacim_deger == "2001-2500 cc"):
        hacim = 6
        mesaj()
    elif(hacim_deger == "5501-6000 cc"):
        hacim = 7
        mesaj()
    elif(hacim_deger == "5001-5500 cc"):
        hacim = 8
        mesaj()
    elif(hacim_deger == "4501-5000 cc"):
        hacim = 9
        mesaj()
    elif(hacim_deger == "3001-3500 cc"):
        hacim = 10
     
    else:
        olumsuz()
           
        
def güç_düzenle():
    global yaş
    güç_deger = güç_kutu.get()
    if(güç_deger == "101-125 BG"):
        güç = 0
        mesaj()
    elif(güç_deger == "76-100 BG"):
        güç = 1
        mesaj()
    elif(güç_deger == "Bilinmiyor"):
        güç = 2
        mesaj()
    elif(güç_deger == "51-75 BG"):
        güç = 3
        mesaj()
    elif(güç_deger == "126-150 BG"):
        güç = 4
        mesaj()
    elif(güç_deger == "176-200 BG"):
        güç = 5
        mesaj()
    elif(güç_deger == "151-175 BG"):
        güç = 7
    elif(güç_deger == "100 BG ve altı"):
        güç = 8
        mesaj()
    elif(güç_deger == "201-225 BG"):
        güç = 9
        mesaj()
    elif(güç_deger == "251-275 BG"):
        güç = 10
        mesaj()
    elif(güç_deger == "401-45 BG"):
        güç = 11
        mesaj()
    elif(güç_deger == "326-350 BG"):
        güç = 12
       
   
    else:
        olumsuz()
  



def kimden_düzenle():
    global kimden
    kimden_deger = kimden_kutu.get()
    if(kimden_deger == "Sahibinden"):
        kimden = 0
        mesaj()
    elif(kimden_deger == "Galeriden"):
        kimden = 1
        mesaj()
    elif(kimden_deger == "Aracıdan"):
        kimden = 2
    
    else:
        olumsuz()
    


    
    
    
    
    
    s2 = Label(pencere, text = pred, font="helvetica 20",borderwidth=6, padx = 200, pady = 40)
    s2.place(x = 1010, y = 300)
        
baslık_label = Label(pencere, text = "ARABA FİYAT TAHMİNİ", font="helvetica 50",borderwidth=20, padx = 550, pady = 40,
                     background = "#FF8000")        
baslık_label.place(x = 70 ,y = 20)
        
        

# MARKA KISMI
Marka_label = Label(text = "Marka Seçimi", font="helvetica 12",borderwidth=6)
Marka_label.place(x = 100, y = 300)

markalar = ["Renault","Volkswagen","Ford","Hyundai","Peugeot","Fiat","Mercedes","Tofaş","Toyota","Opel","Dacia","Honda","Chevrolet","BMW","Audi","Nissan","Mini","Kia","Seat","Land Rover","Citroen","Volvo","Mitsubishi","Jaguar","Skoda","Lada","Subaru","Jeep","Alfa Romeo","Dodge","Tata","Chrysler"]
marka_kutu = Combobox(pencere, values = markalar)
marka_kutu.place(x = 100,y = 350)

marka_buton = Button(pencere, text = "Seç", command = marka_düzenle, font="helvetica 12",borderwidth=6)
marka_buton.place(x = 100, y = 400)
#--------


# MODEL YILI
yıl_label = Label(text = "Model yılını Seçiniz", font="helvetica 12",borderwidth=6)
yıl_label.place(x = 300, y = 300)

yıl = ["2015","2017","2012","2013","2011","2016","2014","2005","2004","2020","2007","2019","2010","2001","1996","2008","2000","1997","2009","2006","1998","2018","1994","1957","1977","1991","1987","2003","2002","1999","1995","2021"     ]
yıl_kutu = Combobox(pencere, values = yıl )
yıl_kutu.place(x = 300, y = 350)

yıl_buton = Button(pencere, text = "Seç", command = yıl_düzenle, font="helvetica 12",borderwidth=6)
yıl_buton.place(x = 300, y = 400)
#---------


# YAKIT TÜRÜ
yakıt_label = Label(text = "Yakıt Türü Seçiniz", font="helvetica 12",borderwidth=6)
yakıt_label.place(x = 500, y = 300)

yakıt = ["Dizel","Benzin/LPG","Benzin","Hibrit","Elektrik"]
yakıt_kutu = Combobox(pencere, values = yakıt)
yakıt_kutu.place(x = 500, y = 350)

yakıt_buton = Button(pencere, text = "Seç", command = yakıt_düzenle, font="helvetica 12",borderwidth=6)
yakıt_buton.place(x = 500, y = 400)
#---------------



# VİTES TÜRÜ
vites_label = Label(text = "Vites Türü Seçiniz", font="helvetica 12",borderwidth=6)
vites_label.place(x = 700, y = 300)
vites = ["Düz Vites","Otomatik Vites","Yarı Otomatik Vites"]
vites_kutu = Combobox(pencere, values = vites)
vites_kutu.place(x = 700, y = 350)

vites_buton = Button(pencere, text = "Seç", command = vites_düzenle, font="helvetica 12",borderwidth=6)
vites_buton.place(x = 700, y = 400)
#---------------------




#MOTOR HACİMİ DURUMU
hacim_label = Label(pencere, text = "Motor Hacimi Seçiniz", font="helvetica 12",borderwidth=6)
hacim_label.place(x = 100, y = 500)

hacim = ["1301-1600 cc","1300 cc ve altı","1801-2000 cc","1601-1800 cc","Bilinmiyor","2501-3000 cc","2001-2500 cc","5501-6000 cc","5001-5500 cc","4501-5000 cc","3001-3500 cc"          ]
hacim_kutu = Combobox(pencere, values = hacim)
hacim_kutu.place(x = 100, y = 550)

hacim_buton = Button(pencere, text = "Seç", command = hacim_düzenle, font="helvetica 12",borderwidth=6)
hacim_buton.place(x = 100, y = 600)
#-------------

# BEYGİR GÜCÜ
güç_label = Label(text = "Beygir Gücünü Seçiniz", font="helvetica 12",borderwidth=6)
güç_label.place(x = 300, y = 500)

güç = ["101-125 BG","76-100 BG","Bilinmiyor","51-75 BG","126-150 BG","176-200 BG","151-175 BG","100 BG ve altı","201-225 BG","251-275 BG","401-45 BG","326-350 BG"  ]
güç_kutu = Combobox(pencere, values = güç)
güç_kutu.place(x = 300, y = 550)

güç_buton = Button(pencere, text = "Seç", command = güç_düzenle, font="helvetica 12",borderwidth=6)
güç_buton.place(x = 300, y = 600)
#------------------


# KM ARAÇ
km_label = Label(text = "KM Giriniz", font="helvetica 12",borderwidth=6)
km_label.place(x = 500, y = 500)

km_entry = Entry()
km_entry.place(x = 500, y = 550)

km_buton = Button(pencere, text = "Seç", command = km_düzenle, font="helvetica 12",borderwidth=6)
km_buton.place(x = 500, y = 600)



# KİMDEN
kimden_label = Label(text = "Arabanın Kimden Alındığını Seçiniz", font="helvetica 12",borderwidth=6)
kimden_label.place(x = 700, y = 500)

kimden = ["Sahibinden","Galeriden","Aracıdan"]
kimden_kutu = Combobox(pencere, values = kimden)
kimden_kutu.place(x = 700, y = 550)

kimden_buton = Button(pencere, text = "Seç", command = kimden_düzenle, font="helvetica 12",borderwidth=6)
kimden_buton.place(x = 700, y = 600)
#---------------------

# ML KISIM BAŞLANGIÇ



def hesapla():
    yeni_veri = [[markalar],[yıl],[yakıt],[vites],[hacim],[güç],[km],[kimden]]  
    yeni_veri = pd.DataFrame(yeni_veri).T

    df_21 = yeni_veri.rename(columns = {
                        0:"Marka",
                        1:"Yıl",
                        2:"yakıt",
                        3:"vites",
                        4:"hacim",
                        5:"güç",
                        6:"km",
                        7:"kimden",
                        
                      })
    
    pred = model_xgb.predict(df_21)
    pred = int(pred)
    s2 = Label(pencere, text = pred, font="helvetica 20",borderwidth=6, padx = 200, pady = 40)
    s2.place(x = 1010, y = 300)
        
    
# HESAPLA
hesapla_buton = Button(pencere, text = "HESAPLA", command = hesapla, font="helvetica 15",borderwidth=60, padx = 100, pady = 40, background = "#f7fafc")
hesapla_buton.place(x = 1010, y = 500)

s1 = Label(pencere, text= "125000", font="helvetica 12",borderwidth=6, padx = 200, pady = 40)
s1.place(x = 1010, y = 300)



# HAKKINDA


hakkında_label = Label(pencere, text = "FATİH KARAMEŞE", font="helvetica 20",borderwidth=10, background = "#CC0000")       
hakkında_label.place(x = 100, y = 690)
 
hakkında_label = Label(pencere, text = "KONYA TEKNİK ÜNİVERSİTESİ", font="helvetica 20",borderwidth=10, background = "#CC0000")  
hakkında_label.place(x = 100, y = 730)


mainloop()

df.head()