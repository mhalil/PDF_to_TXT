import re

##### Desen İsimlerini Guncelleyen Fonksiyon ###################
desen_listesi = []
pattern = r'\w+\s+=\s+r"'

def desen_listesini_guncelle():
    with open("desenler.py", "r", encoding="utf8") as dosya:
        icerik = dosya.read()
        eslesme = re.findall(pattern, icerik)
        for desen_adi in eslesme:
            desen_listesi.append(desen_adi[:-5])

desen_listesini_guncelle()

# ### Desen isimlerini ekrana yazdır, kontrol et.
for i in desen_listesi:
    print(desen_listesi.index(i)+1 , i)
###############################################################   