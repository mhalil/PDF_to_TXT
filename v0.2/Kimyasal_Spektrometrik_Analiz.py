import re

##### Spektrometrik (Kimyasal) Analiz Deseni #####################################################################################################################
desen_kimyasal = r"\*?\w+\s+<?\d+\.\d+\s+%\s+ASTM E1999"      # Örnek eslesme: "*Mg  0.040  %  ASTM E1999", "C  3.688  %  ASTM E1999 " ya da "Ni  <0.010  %  ASTM E1999 "
###############################################################################################################################################################################

##### "pdf_verisi.txt" isimli dosya içeriğini oku, desen ile eşleşen değerleri Konsola yazdır. ####
def yazdir():
    with open("pdf_verisi.txt", "r", encoding="utf8") as dosya:
        icerik = dosya.read()
        eslesme = re.findall(desen_kimyasal, icerik)
        for deger in eslesme:
            print("Spektrometrik (Kimyasal) Analiz - " + deger)      # esleşen değerleri alt alta yazdır, ekrana bas.
#####################################################################################################

##### "pdf_verisi.txt" isimli dosya içeriğini oku, desen ile eşleşen değerleri "Rapor_Degerleri.txt" isimli dosyaya ekle / kaydet. ####
def kaydet():
    with open("pdf_verisi.txt", "r", encoding="utf8") as dosya:
        icerik = dosya.read()
        eslesme = re.findall(desen_kimyasal, icerik)
        with open("Rapor_Degerleri.txt", "a", encoding="utf8") as kaydet:
            for deger in eslesme:
                kaydet.write("Spektrometrik (Kimyasal) Analiz - " + deger.replace(".", ",") + "\n")    # "." nokta karakterini "," virgül ile değiştir, sonra kaydet.
#######################################################################################################################################