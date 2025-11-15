import re, fonksiyonlar, desenler, desen_isimleri
from fonksiyonlar import *
from desenler import *

##### Desen Listesini Güncelleyen Fonksiyonu Çalıştır #####
desen_isimleri.desen_listesini_guncelle()

##### Desen Listesini Yeni Listeye Ata ######
d_listesi = desen_isimleri.desen_listesi

### Desen listesini sırası ile ekrana yazdır ##############
# for desen_adi in d_listesi:
#     print(d_listesi.index(desen_adi)+1, desen_adi)
#############################################################

##### ÇÖZÜM 1 - Yazbel'den semtex'in cevabı
##### Fonksiyonlar ##########################################
def raporu_yazdir1():
    for desen_adi in d_listesi:
        desen_adi_string = str(desen_adi)
        desen_degeri = globals()[desen_adi_string]
        yazdir(desen_degeri)

def raporu_kaydet1():
    for desen_adi in d_listesi:
        desen_adi_string = str(desen_adi)
        desen_degeri = globals()[desen_adi_string]
        kaydet(desen_degeri)

# ##### 1. Fonksiyonları Çalıştır #####
# raporu_yazdir1()
# raporu_kaydet1()
#####################################


##### ÇÖZÜM 2 - Yazbel'den aib'in cevabı: ###################
def raporu_yazdir2():
    for desen_adi in d_listesi:
        fonksiyonlar.yazdir(getattr(desenler, desen_adi))

def raporu_kaydet2():
    for desen_adi in d_listesi:
        fonksiyonlar.kaydet(getattr(desenler, desen_adi))

##### 2. Fonksiyonları Çalıştır #####
raporu_yazdir2()
# raporu_kaydet2()
#####################################
