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

##### Dökme Demir Spektrometrik (Kimyasal) Analiz Deseni #####################################################################################################################
desen_dokme_demir = r"\*?\w+\s+<?\d+\.\d+\s+%\s+ASTM E1999"      # Örnek eslesme: "*Mg  0.040  %  ASTM E1999", "C  3.688  %  ASTM E1999 " ya da "Ni  <0.010  %  ASTM E1999 "
###############################################################################################################################################################################

##### "pdf_verisi.txt" isimli dosya içeriğini oku, desen ile eşleşen değerleri "Dökme_Demir_ASTM_E1999_Kimyasal.txt" isimli dosyaya kaydet. #############
with open("pdf_verisi.txt", "r", encoding="utf8") as dosya:
    icerik = dosya.read()
    eslesme = re.findall(desen_dokme_demir, icerik)

    for deger in eslesme:
        print(deger)      # esleşen değerleri alt alta yazdır, ekrana bas.

    # with open("Dökme_Demir_ASTM_E1999_Kimyasal.txt", "w", encoding="utf8") as kaydet:
    #    for deger in eslesme:
    #         kaydet.write(deger.replace(".", ",") + "\n")    # "." nokta karakterini "," virgül ile değiştir, sonra kaydet.
#########################################################################################################################################################
