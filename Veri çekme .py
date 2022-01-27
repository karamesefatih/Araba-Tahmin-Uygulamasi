# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 14:45:56 2021

@author: karamesefatih
"""


from selenium import webdriver
import time
import pandas as pd


# Bu hazır fonksyonumuz adından da anlaşılacağı üzere listeyi string türüne çeviriyor.
def listToString(s):  
    
    # initialize an empty string 
    str1 = " " 
    
    # return string   
    return (str1.join(s)) 

# Bu aşamada selenium ile veri çekmeye başlıyoruz.

# chrome driverin yolunu veriyoruz. Selenium u kullanmak için gereklidir.
driver_path = "D:\PROGRAM SETUP\chromedriver.exe"
# browser adında bi değişken oluşturuyoruz ve driver yolumuzu veriyoruz. Bunu ortam değişkenlerine eklememiz gerekiyor öncesinde
browser = webdriver.Chrome(driver_path)
# browser get ile verdiğimiz adres de ki web sitesine gitmiş oluyoruz.

browser.get("https://www.tasit.com/otomobil/yer/ankara?sayfa=6")

# şimdi bu sayfa içinde her linke tıklayarak verileri çekeceğiz sonra o sayfadan çıkıp bi altında ki evin linke girip onun 
# verilerini alarak sırayla bu işlemi devam ettireceğiz.

# Şuan da web sitesinin arayüzündeyiz. Amacımız arabaların detaylarına bakmak için linke tıklamak. Bunu da xpathlere göre yapacağız
# neden hepsini tek döngü de yapmadık. çünkü arada reklamlar olduğu için pathler karışıyor. Reklamları atlamak için
# böyle bi yol izledim.
i = 3
while i <= 4:
    # tıkla adında değişkene find diyerek bu xpath de 1. olana gidiyor.
    tıkla = browser.find_element_by_xpath("//*[@id='park_or_compare']/table/tbody/tr["+str(i)+"]")
    # click diyerek de bu linke tıklıyor ve evin detaylarına bakmak için sayfaya girmiş oluyoruz.
    tıkla.click()
    # özelliklerin hepsini almak için bu sefer bu kod ile orda ki css bloğuna göre veriyi çekeceğiz.
    elements = browser.find_elements_by_css_selector(".offer-info-container")
    # özellikleri bir önceki kodda aldık şimdi de evin fiyatını alıyoruz ve değişkene kaydediyoruz.
    fiyatlar = browser.find_elements_by_css_selector(".offer-price")
    
    # 2 tane boş liste oluşturuyoruz. Elimizde ki dağınık veriyi düzenleyip listeye atacağız.
    detaylar = []
    fiyat = []
    # çektiğimiz veriler text string olmadığı için verileri stringe çevirip demin oluşturduğumuz boş listeye atıyoruz.
    # unutmayalım ki verileri çektiğiniz de liste olarak gelir.
    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)
    # özellikleri de stringe çevirerek listeye atıyoruz.
    for i in elements:
        print(i.text)
        detaylar.append(i.text)
        
    det_str = listToString(detaylar)
    # string verimizi split ile satırlara göre ayırıyoruz. Ve ayrı adında değişkene atıyoruz.
    ayrı = det_str.split("\n")
    # demin oluşturduğumuz ayrı değişkenini DataFrame çeviriyoruz. 
    df = pd.DataFrame(ayrı)
    # Verimizde ki gereksiz verilerden kurtulmak için onları ayırıyoruz.
    df_yeni = df.iloc[2:24]
    df_yeni.iloc[21] = df_yeni.iloc[21].str[0:3]
    # değişiklikler yaptığımız için indexleri resetliyoruz.
    df_yeni = df_yeni.reset_index()
    # gereksiz oluşan şndex sütununu siliyoruz.
    df_yeni.drop("index", axis = 1, inplace = True)
    # verilerimizi tekrar listeye çeviriyorum.
    df_liste = df_yeni.values.tolist()
    # içerikler adında boş liste oluşturuyprum amacım şu şuan elimizde ki veri sütun adlarını ve içeriklerini barındırıyor.
    # içerikleri sütun adlarından ayırmak için bu işlemi yapıyoruz.
    içerikler =[]
    i = 1
    while i <= 21:
        print(df_liste[i])
        içerikler.append(df_liste[i])
        i = i + 2
    # Hatırlarsanız fiyatı başka bi yerde çekmiştik ve bunu da içeriklere yeni bi sütuna ekliyoruz.
    # öncesinde fiyat değişkeninde ki gereksiz verileri siliyoruz. TL yazısını ve strip ile gereksiz boşlukları
    fiyat_sade = fiyat[0].strip()
    fiyat_sade = fiyat_sade.replace("TL","")
    # içerikler kısmına fiyatı ekliyoruz.
    içerikler.append([fiyat_sade])
    # şuan liste halinde olan verimizi Df e çeviriyoruz ve transpozunu alıyoruz.
    df_içerikler = pd.DataFrame(içerikler).T
    # verimizi csv dosyasına çeviriyoruz ve modu append yapıyoruz. Çünkü diğer çektiğimiz verileri de oraya ekleyeceğiz.
    # eğer mode = a yapmassak diğer gelen veriyi üzerine yazacaktır.
    df_içerikler.to_csv(r"database.csv",encoding="utf-8",index=False, mode="a")
    
    # i değişkeni sayfada ki evlerin xpath de ki sayısıydı
    
    i = i+1
    # bu kod ile bi önceki sayfaya geçiyoruz.
    browser.execute_script("window.history.go(-1)")

print("1. kısım çalıştı")


i = 7
while i <= 8:
    # tıkla adında değişkene find diyerek bu xpath de 1. olana gidiyor.
    tıkla = browser.find_element_by_xpath("//*[@id='park_or_compare']/table/tbody/tr["+str(i)+"]")
    # click diyerek de bu linke tıklıyor ve evin detaylarına bakmak için sayfaya girmiş oluyoruz.
    tıkla.click()
    # özelliklerin hepsini almak için bu sefer bu kod ile orda ki css bloğuna göre veriyi çekeceğiz.
    elements = browser.find_elements_by_css_selector(".offer-info-container")
    # özellikleri bir önceki kodda aldık şimdi de evin fiyatını alıyoruz ve değişkene kaydediyoruz.
    fiyatlar = browser.find_elements_by_css_selector(".offer-price")
    
    # 2 tane boş liste oluşturuyoruz. Elimizde ki dağınık veriyi düzenleyip listeye atacağız.
    detaylar = []
    fiyat = []
    # çektiğimiz veriler text string olmadığı için verileri stringe çevirip demin oluşturduğumuz boş listeye atıyoruz.
    # unutmayalım ki verileri çektiğiniz de liste olarak gelir.
    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)
    # özellikleri de stringe çevirerek listeye atıyoruz.
    for i in elements:
        print(i.text)
        detaylar.append(i.text)
        
    det_str = listToString(detaylar)
    # string verimizi split ile satırlara göre ayırıyoruz. Ve ayrı adında değişkene atıyoruz.
    ayrı = det_str.split("\n")
    # demin oluşturduğumuz ayrı değişkenini DataFrame çeviriyoruz. 
    df = pd.DataFrame(ayrı)
    # Verimizde ki gereksiz verilerden kurtulmak için onları ayırıyoruz.
    df_yeni = df.iloc[2:24]
    df_yeni.iloc[21] = df_yeni.iloc[21].str[0:3]
    # değişiklikler yaptığımız için indexleri resetliyoruz.
    df_yeni = df_yeni.reset_index()
    # gereksiz oluşan şndex sütununu siliyoruz.
    df_yeni.drop("index", axis = 1, inplace = True)
    # verilerimizi tekrar listeye çeviriyorum.
    df_liste = df_yeni.values.tolist()
    # içerikler adında boş liste oluşturuyprum amacım şu şuan elimizde ki veri sütun adlarını ve içeriklerini barındırıyor.
    # içerikleri sütun adlarından ayırmak için bu işlemi yapıyoruz.
    içerikler =[]
    i = 1
    while i <= 21:
        print(df_liste[i])
        içerikler.append(df_liste[i])
        i = i + 2
    # Hatırlarsanız fiyatı başka bi yerde çekmiştik ve bunu da içeriklere yeni bi sütuna ekliyoruz.
    # öncesinde fiyat değişkeninde ki gereksiz verileri siliyoruz. TL yazısını ve strip ile gereksiz boşlukları
    fiyat_sade = fiyat[0].strip()
    fiyat_sade = fiyat_sade.replace("TL","")
    # içerikler kısmına fiyatı ekliyoruz.
    içerikler.append([fiyat_sade])
    # şuan liste halinde olan verimizi Df e çeviriyoruz ve transpozunu alıyoruz.
    df_içerikler = pd.DataFrame(içerikler).T
    # verimizi csv dosyasına çeviriyoruz ve modu append yapıyoruz. Çünkü diğer çektiğimiz verileri de oraya ekleyeceğiz.
    # eğer mode = a yapmassak diğer gelen veriyi üzerine yazacaktır.
    df_içerikler.to_csv(r"database.csv",encoding="utf-8",index=False, mode="a")
    
    # i değişkeni sayfada ki evlerin xpath de ki sayısıydı
    
    i = i+1
    # bu kod ile bi önceki sayfaya geçiyoruz.
    browser.execute_script("window.history.go(-1)")




print("2. kısım çalıştı")
i = 11
while i <= 12:
    # tıkla adında değişkene find diyerek bu xpath de 1. olana gidiyor.
    tıkla = browser.find_element_by_xpath("//*[@id='park_or_compare']/table/tbody/tr["+str(i)+"]")
    # click diyerek de bu linke tıklıyor ve evin detaylarına bakmak için sayfaya girmiş oluyoruz.
    tıkla.click()
    # özelliklerin hepsini almak için bu sefer bu kod ile orda ki css bloğuna göre veriyi çekeceğiz.
    elements = browser.find_elements_by_css_selector(".offer-info-container")
    # özellikleri bir önceki kodda aldık şimdi de evin fiyatını alıyoruz ve değişkene kaydediyoruz.
    fiyatlar = browser.find_elements_by_css_selector(".offer-price")
    
    # 2 tane boş liste oluşturuyoruz. Elimizde ki dağınık veriyi düzenleyip listeye atacağız.
    detaylar = []
    fiyat = []
    # çektiğimiz veriler text string olmadığı için verileri stringe çevirip demin oluşturduğumuz boş listeye atıyoruz.
    # unutmayalım ki verileri çektiğiniz de liste olarak gelir.
    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)
    # özellikleri de stringe çevirerek listeye atıyoruz.
    for i in elements:
        print(i.text)
        detaylar.append(i.text)
        
    det_str = listToString(detaylar)
    # string verimizi split ile satırlara göre ayırıyoruz. Ve ayrı adında değişkene atıyoruz.
    ayrı = det_str.split("\n")
    # demin oluşturduğumuz ayrı değişkenini DataFrame çeviriyoruz. 
    df = pd.DataFrame(ayrı)
    # Verimizde ki gereksiz verilerden kurtulmak için onları ayırıyoruz.
    df_yeni = df.iloc[2:24]
    df_yeni.iloc[21] = df_yeni.iloc[21].str[0:3]
    # değişiklikler yaptığımız için indexleri resetliyoruz.
    df_yeni = df_yeni.reset_index()
    # gereksiz oluşan şndex sütununu siliyoruz.
    df_yeni.drop("index", axis = 1, inplace = True)
    # verilerimizi tekrar listeye çeviriyorum.
    df_liste = df_yeni.values.tolist()
    # içerikler adında boş liste oluşturuyprum amacım şu şuan elimizde ki veri sütun adlarını ve içeriklerini barındırıyor.
    # içerikleri sütun adlarından ayırmak için bu işlemi yapıyoruz.
    içerikler =[]
    i = 1
    while i <= 21:
        print(df_liste[i])
        içerikler.append(df_liste[i])
        i = i + 2
    # Hatırlarsanız fiyatı başka bi yerde çekmiştik ve bunu da içeriklere yeni bi sütuna ekliyoruz.
    # öncesinde fiyat değişkeninde ki gereksiz verileri siliyoruz. TL yazısını ve strip ile gereksiz boşlukları
    fiyat_sade = fiyat[0].strip()
    fiyat_sade = fiyat_sade.replace("TL","")
    # içerikler kısmına fiyatı ekliyoruz.
    içerikler.append([fiyat_sade])
    # şuan liste halinde olan verimizi Df e çeviriyoruz ve transpozunu alıyoruz.
    df_içerikler = pd.DataFrame(içerikler).T
    # verimizi csv dosyasına çeviriyoruz ve modu append yapıyoruz. Çünkü diğer çektiğimiz verileri de oraya ekleyeceğiz.
    # eğer mode = a yapmassak diğer gelen veriyi üzerine yazacaktır.
    df_içerikler.to_csv(r"database.csv",encoding="utf-8",index=False, mode="a")
    
    # i değişkeni sayfada ki evlerin xpath de ki sayısıydı
    
    i = i+1
    # bu kod ile bi önceki sayfaya geçiyoruz.
    browser.execute_script("window.history.go(-1)")

print("3. kısım çalıştı")
i = 14
while i <= 15:
    # tıkla adında değişkene find diyerek bu xpath de 1. olana gidiyor.
    tıkla = browser.find_element_by_xpath("//*[@id='park_or_compare']/table/tbody/tr["+str(i)+"]")
    # click diyerek de bu linke tıklıyor ve evin detaylarına bakmak için sayfaya girmiş oluyoruz.
    tıkla.click()
    # özelliklerin hepsini almak için bu sefer bu kod ile orda ki css bloğuna göre veriyi çekeceğiz.
    elements = browser.find_elements_by_css_selector(".offer-info-container")
    # özellikleri bir önceki kodda aldık şimdi de evin fiyatını alıyoruz ve değişkene kaydediyoruz.
    fiyatlar = browser.find_elements_by_css_selector(".offer-price")
    
    # 2 tane boş liste oluşturuyoruz. Elimizde ki dağınık veriyi düzenleyip listeye atacağız.
    detaylar = []
    fiyat = []
    # çektiğimiz veriler text string olmadığı için verileri stringe çevirip demin oluşturduğumuz boş listeye atıyoruz.
    # unutmayalım ki verileri çektiğiniz de liste olarak gelir.
    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)
    # özellikleri de stringe çevirerek listeye atıyoruz.
    for i in elements:
        print(i.text)
        detaylar.append(i.text)
        
    det_str = listToString(detaylar)
    # string verimizi split ile satırlara göre ayırıyoruz. Ve ayrı adında değişkene atıyoruz.
    ayrı = det_str.split("\n")
    # demin oluşturduğumuz ayrı değişkenini DataFrame çeviriyoruz. 
    df = pd.DataFrame(ayrı)
    # Verimizde ki gereksiz verilerden kurtulmak için onları ayırıyoruz.
    df_yeni = df.iloc[2:24]
    df_yeni.iloc[21] = df_yeni.iloc[21].str[0:3]
    # değişiklikler yaptığımız için indexleri resetliyoruz.
    df_yeni = df_yeni.reset_index()
    # gereksiz oluşan şndex sütununu siliyoruz.
    df_yeni.drop("index", axis = 1, inplace = True)
    # verilerimizi tekrar listeye çeviriyorum.
    df_liste = df_yeni.values.tolist()
    # içerikler adında boş liste oluşturuyprum amacım şu şuan elimizde ki veri sütun adlarını ve içeriklerini barındırıyor.
    # içerikleri sütun adlarından ayırmak için bu işlemi yapıyoruz.
    içerikler =[]
    i = 1
    while i <= 21:
        print(df_liste[i])
        içerikler.append(df_liste[i])
        i = i + 2
    # Hatırlarsanız fiyatı başka bi yerde çekmiştik ve bunu da içeriklere yeni bi sütuna ekliyoruz.
    # öncesinde fiyat değişkeninde ki gereksiz verileri siliyoruz. TL yazısını ve strip ile gereksiz boşlukları
    fiyat_sade = fiyat[0].strip()
    fiyat_sade = fiyat_sade.replace("TL","")
    # içerikler kısmına fiyatı ekliyoruz.
    içerikler.append([fiyat_sade])
    # şuan liste halinde olan verimizi Df e çeviriyoruz ve transpozunu alıyoruz.
    df_içerikler = pd.DataFrame(içerikler).T
    # verimizi csv dosyasına çeviriyoruz ve modu append yapıyoruz. Çünkü diğer çektiğimiz verileri de oraya ekleyeceğiz.
    # eğer mode = a yapmassak diğer gelen veriyi üzerine yazacaktır.
    df_içerikler.to_csv(r"database.csv",encoding="utf-8",index=False, mode="a")
    
    # i değişkeni sayfada ki evlerin xpath de ki sayısıydı
    
    i = i+1
    # bu kod ile bi önceki sayfaya geçiyoruz.
    browser.execute_script("window.history.go(-1)")

print("4. kısım çalıştı")

i = 17
while i <= 18:
    # tıkla adında değişkene find diyerek bu xpath de 1. olana gidiyor.
    tıkla = browser.find_element_by_xpath("//*[@id='park_or_compare']/table/tbody/tr["+str(i)+"]")
    # click diyerek de bu linke tıklıyor ve evin detaylarına bakmak için sayfaya girmiş oluyoruz.
    tıkla.click()
    # özelliklerin hepsini almak için bu sefer bu kod ile orda ki css bloğuna göre veriyi çekeceğiz.
    elements = browser.find_elements_by_css_selector(".offer-info-container")
    # özellikleri bir önceki kodda aldık şimdi de evin fiyatını alıyoruz ve değişkene kaydediyoruz.
    fiyatlar = browser.find_elements_by_css_selector(".offer-price")
    
    # 2 tane boş liste oluşturuyoruz. Elimizde ki dağınık veriyi düzenleyip listeye atacağız.
    detaylar = []
    fiyat = []
    # çektiğimiz veriler text string olmadığı için verileri stringe çevirip demin oluşturduğumuz boş listeye atıyoruz.
    # unutmayalım ki verileri çektiğiniz de liste olarak gelir.
    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)
    # özellikleri de stringe çevirerek listeye atıyoruz.
    for i in elements:
        print(i.text)
        detaylar.append(i.text)
        
    det_str = listToString(detaylar)
    # string verimizi split ile satırlara göre ayırıyoruz. Ve ayrı adında değişkene atıyoruz.
    ayrı = det_str.split("\n")
    # demin oluşturduğumuz ayrı değişkenini DataFrame çeviriyoruz. 
    df = pd.DataFrame(ayrı)
    # Verimizde ki gereksiz verilerden kurtulmak için onları ayırıyoruz.
    df_yeni = df.iloc[2:24]
    df_yeni.iloc[21] = df_yeni.iloc[21].str[0:3]
    # değişiklikler yaptığımız için indexleri resetliyoruz.
    df_yeni = df_yeni.reset_index()
    # gereksiz oluşan şndex sütununu siliyoruz.
    df_yeni.drop("index", axis = 1, inplace = True)
    # verilerimizi tekrar listeye çeviriyorum.
    df_liste = df_yeni.values.tolist()
    # içerikler adında boş liste oluşturuyprum amacım şu şuan elimizde ki veri sütun adlarını ve içeriklerini barındırıyor.
    # içerikleri sütun adlarından ayırmak için bu işlemi yapıyoruz.
    içerikler =[]
    i = 1
    while i <= 21:
        print(df_liste[i])
        içerikler.append(df_liste[i])
        i = i + 2
    # Hatırlarsanız fiyatı başka bi yerde çekmiştik ve bunu da içeriklere yeni bi sütuna ekliyoruz.
    # öncesinde fiyat değişkeninde ki gereksiz verileri siliyoruz. TL yazısını ve strip ile gereksiz boşlukları
    fiyat_sade = fiyat[0].strip()
    fiyat_sade = fiyat_sade.replace("TL","")
    # içerikler kısmına fiyatı ekliyoruz.
    içerikler.append([fiyat_sade])
    # şuan liste halinde olan verimizi Df e çeviriyoruz ve transpozunu alıyoruz.
    df_içerikler = pd.DataFrame(içerikler).T
    # verimizi csv dosyasına çeviriyoruz ve modu append yapıyoruz. Çünkü diğer çektiğimiz verileri de oraya ekleyeceğiz.
    # eğer mode = a yapmassak diğer gelen veriyi üzerine yazacaktır.
    df_içerikler.to_csv(r"database.csv",encoding="utf-8",index=False, mode="a")
    
    # i değişkeni sayfada ki evlerin xpath de ki sayısıydı
    
    i = i+1
    # bu kod ile bi önceki sayfaya geçiyoruz.
    browser.execute_script("window.history.go(-1)")

print("5. kısım çalıştı")

i = 20
while i <= 21:
    # tıkla adında değişkene find diyerek bu xpath de 1. olana gidiyor.
    tıkla = browser.find_element_by_xpath("//*[@id='park_or_compare']/table/tbody/tr["+str(i)+"]")
    # click diyerek de bu linke tıklıyor ve evin detaylarına bakmak için sayfaya girmiş oluyoruz.
    tıkla.click()
    # özelliklerin hepsini almak için bu sefer bu kod ile orda ki css bloğuna göre veriyi çekeceğiz.
    elements = browser.find_elements_by_css_selector(".offer-info-container")
    # özellikleri bir önceki kodda aldık şimdi de evin fiyatını alıyoruz ve değişkene kaydediyoruz.
    fiyatlar = browser.find_elements_by_css_selector(".offer-price")
    
    # 2 tane boş liste oluşturuyoruz. Elimizde ki dağınık veriyi düzenleyip listeye atacağız.
    detaylar = []
    fiyat = []
    # çektiğimiz veriler text string olmadığı için verileri stringe çevirip demin oluşturduğumuz boş listeye atıyoruz.
    # unutmayalım ki verileri çektiğiniz de liste olarak gelir.
    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)
    # özellikleri de stringe çevirerek listeye atıyoruz.
    for i in elements:
        print(i.text)
        detaylar.append(i.text)
        
    det_str = listToString(detaylar)
    # string verimizi split ile satırlara göre ayırıyoruz. Ve ayrı adında değişkene atıyoruz.
    ayrı = det_str.split("\n")
    # demin oluşturduğumuz ayrı değişkenini DataFrame çeviriyoruz. 
    df = pd.DataFrame(ayrı)
    # Verimizde ki gereksiz verilerden kurtulmak için onları ayırıyoruz.
    df_yeni = df.iloc[2:24]
    df_yeni.iloc[21] = df_yeni.iloc[21].str[0:3]
    # değişiklikler yaptığımız için indexleri resetliyoruz.
    df_yeni = df_yeni.reset_index()
    # gereksiz oluşan şndex sütununu siliyoruz.
    df_yeni.drop("index", axis = 1, inplace = True)
    # verilerimizi tekrar listeye çeviriyorum.
    df_liste = df_yeni.values.tolist()
    # içerikler adında boş liste oluşturuyprum amacım şu şuan elimizde ki veri sütun adlarını ve içeriklerini barındırıyor.
    # içerikleri sütun adlarından ayırmak için bu işlemi yapıyoruz.
    içerikler =[]
    i = 1
    while i <= 21:
        print(df_liste[i])
        içerikler.append(df_liste[i])
        i = i + 2
    # Hatırlarsanız fiyatı başka bi yerde çekmiştik ve bunu da içeriklere yeni bi sütuna ekliyoruz.
    # öncesinde fiyat değişkeninde ki gereksiz verileri siliyoruz. TL yazısını ve strip ile gereksiz boşlukları
    fiyat_sade = fiyat[0].strip()
    fiyat_sade = fiyat_sade.replace("TL","")
    # içerikler kısmına fiyatı ekliyoruz.
    içerikler.append([fiyat_sade])
    # şuan liste halinde olan verimizi Df e çeviriyoruz ve transpozunu alıyoruz.
    df_içerikler = pd.DataFrame(içerikler).T
    # verimizi csv dosyasına çeviriyoruz ve modu append yapıyoruz. Çünkü diğer çektiğimiz verileri de oraya ekleyeceğiz.
    # eğer mode = a yapmassak diğer gelen veriyi üzerine yazacaktır.
    df_içerikler.to_csv(r"database.csv",encoding="utf-8",index=False, mode="a")
    
    # i değişkeni sayfada ki evlerin xpath de ki sayısıydı
    
    i = i+1
    # bu kod ile bi önceki sayfaya geçiyoruz.
    browser.execute_script("window.history.go(-1)")

print("6. kısım çalıştı")
