import re

##### "pdf_verisi.txt" isimli dosya içeriğini oku, desen ile eşleşen değerleri Konsola yazdır. ####
def yazdir(desen):
    with open("pdf_verisi.txt", "r", encoding="utf8") as dosya:
        icerik = dosya.read()
        eslesme = re.finditer(desen, icerik)
        for eslesen in eslesme:
            print(eslesen.group())


##### "pdf_verisi.txt" isimli dosya içeriğini oku, desen ile eşleşen değerleri "Rapor_Degerleri.txt" isimli dosyaya ekle / kaydet. ####
def kaydet(desen):
    with open("pdf_verisi.txt", "r", encoding="utf8") as dosya:
        icerik = dosya.read()
        eslesme = re.finditer(desen, icerik)
        with open("Rapor_Degerleri.txt", "a", encoding="utf8") as kaydet:
            for eslesen in eslesme:
                kaydet.write(eslesen.group().replace(".", ",") + "\n")    # "." nokta karakterini "," virgül ile değiştir, sonra kaydet.




