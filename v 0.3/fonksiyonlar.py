import re, desenler

##### "pdf_verisi.txt" isimli dosya içeriğini oku, desen ile eşleşen değerleri Konsola yazdır. ####
def yazdir(desen):
    with open("pdf_verisi.txt", "r", encoding="utf8") as dosya:
        icerik = dosya.read()
        eslesme = re.findall(desen, icerik)
        for deger in eslesme:
            print(deger)      # esleşen değerleri alt alta yazdır, ekrana bas.  
####################################################################################################

##### "pdf_verisi.txt" isimli dosya içeriğini oku, desen ile eşleşen değerleri "Rapor_Degerleri.txt" isimli dosyaya ekle / kaydet. ####
def kaydet(desen):
    with open("pdf_verisi.txt", "r", encoding="utf8") as dosya:
        icerik = dosya.read()
        eslesme = re.findall(desen, icerik)
        with open("Rapor_Degerleri.txt", "a", encoding="utf8") as kaydet:
            for deger in eslesme:
                kaydet.write(deger.replace(".", ",") + "\n")    # "." nokta karakterini "," virgül ile değiştir, sonra kaydet.
########################################################################################################################################

# yazdir(desenler.desen_brinell_sertlik)