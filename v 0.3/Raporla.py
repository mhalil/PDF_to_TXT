import PDF_to_TXT       # "veriyi_kaydet()" fonksiyonunu sadece bir kez çalıştırıp PDF Dosya içeriğini "pdf_verisi.txt" adıyla kaydetmek için kullanacağız.
import re, fonksiyonlar

##### PDF_to_TXT.py dosyasındaki "veriyi_kaydet()" fonksiyonunu çalıştır ###
# PDF_to_TXT.veriyi_kaydet()    # 1 kez çalıştırılmalı
############################################################################

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
    print(i)
###############################################################    

#### Fonksiyonları sırayla çalıştır ############
# for desen_adi in desen_listesi:
#     fonksiyonlar.yazdir(desen_adi)
################################################    
