import re, fonksiyonlar, desenler
from fonksiyonlar import *
from desenler import *
import pdf_to_txt

##### "pdf_verisi.txt" ve "Rapor_Degerleri.txt" dosyalarını sil  ##############
sil()
##### ##### ##### ##### #####

desen_listesi = []
pattern = r'\w+\s+=\s+r"'

##### Desen Listesini Güncelleyen Fonksiyon #################
def desen_listesini_guncelle():
	with open("desenler.py", "r", encoding="utf8") as dosya:
		icerik = dosya.read()
		eslesme = re.findall(pattern, icerik)
		for desen_adi in eslesme:
			desen_listesi.append(desen_adi[:-5])

desen_listesini_guncelle()
##### ##### ##### ##### #####

##### Desen listesini sırası ile ekrana yazdır ##############
# for desen_adi in desen_listesi:
#	 print(desen_listesi.index(desen_adi)+1, desen_adi)
##### ##### ##### ##### #####

##### PDF Dosya içeriğini "pdf_verisi.txt" adıyla kaydeden Fonksiyonu çalıştır. ######
pdf_to_txt.pdf_dosya_adi()
##### ##### ##### ##### #####

##### ÇÖZÜM 1 - Yazbel'den semtex'in cevabı
##### Fonksiyonlar ##########################################
def raporu_yazdir1():
	for desen_adi in desen_listesi:
		desen_adi_string = str(desen_adi)
		desen_degeri = globals()[desen_adi_string]
		yazdir(desen_degeri)

def raporu_kaydet1():
	for desen_adi in desen_listesi:
		desen_adi_string = str(desen_adi)
		desen_degeri = globals()[desen_adi_string]
		kaydet(desen_degeri)

# ##### 1. Fonksiyonları Çalıştır #####
raporu_yazdir1()
raporu_kaydet1()
##### ##### ##### ##### #####


##### ÇÖZÜM 2 - Yazbel'den aib'in cevabı: ###################
# def raporu_yazdir2():
#	 for desen_adi in desen_listesi:
#		 fonksiyonlar.yazdir(getattr(desenler, desen_adi))

# def raporu_kaydet2():
#	 for desen_adi in desen_listesi:
#		 fonksiyonlar.kaydet(getattr(desenler, desen_adi))

# ##### 2. Fonksiyonları Çalıştır #####
# raporu_yazdir2()
# raporu_kaydet2()
##### ##### ##### ##### #####
