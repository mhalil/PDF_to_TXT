from PyPDF2 import PdfReader
import re

##### PDF Dosyasına ait Değişken Tanımları ####################
pdf_dosya_adi = "Analiz_Rapor"
pdf_icerigi = PdfReader(pdf_dosya_adi + ".pdf")
toplam_safya_sayisi = len(pdf_icerigi.pages)
###############################################################

##### PDF Dosya içeriğini "pdf_verisi.txt" adıyla kaydet. #####
for sayfa in range(toplam_safya_sayisi):
    with open("pdf_verisi.txt", "a+", encoding="utf8") as dosya:
        dosya.write(pdf_icerigi.pages[sayfa].extract_text())
###############################################################

##### Paslanmaz Çelik Spektrometrik (Kimyasal) Analiz Deseni ####################################################################################
desen_paslanmaz_celik = r"\w+\+?\w+\s+\d+\.\d+\s+%\s+ASTM E1086"      # Örnek eslesme: "C  0.016  %  ASTM E1086" ya da "Cr  18.19  %  ASTM E1086"
#################################################################################################################################################

##### "pdf_verisi.txt" isimli dosya içeriğini oku, desen ile eşleşen değerleri "PaslanmazCelik_ASTM_E1086.txt" isimli dosyaya kaydet. ###
with open("pdf_verisi.txt", "r", encoding="utf8") as dosya:
    icerik = dosya.read()
    eslesme = re.findall(desen_paslanmaz_celik, icerik)

    for deger in eslesme:
        print(deger)      # esleşen değerleri alt alta yazdır, ekrana bas.

    # with open("PaslanmazCelik_ASTM_E1086_Kimyasal.txt", "w", encoding="utf8") as kaydet:
    #    for deger in eslesme:
    #         kaydet.write(deger.replace(".", ",") + "\n")    # "." nokta karakterini "," virgül ile değiştir, sonra kaydet.
#########################################################################################################################################
