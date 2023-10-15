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

##### Brinell_Sertlik Test Sonucu Deseni #######################################################################################
desen_brinell_sertlik = r"Brinell\s+\d+\.\d+\s+HBW"      # Örnek eslesme: "Brinell   195.10  HBW 2,5/187,5  EN ISO 6506-1"
################################################################################################################################

##### "pdf_verisi.txt" isimli dosya içeriğini oku, desen ile eşleşen değerleri "Brinell_Sertlik.txt" isimli dosyaya kaydet. ####
with open("pdf_verisi.txt", "r", encoding="utf8") as dosya:
    icerik = dosya.read()
    eslesme = re.findall(desen_brinell_sertlik, icerik)

    for deger in eslesme:
        print(deger)      # esleşen değerleri alt alta yazdır, ekrana bas.

    # with open("Brinell_Sertlik.txt", "w", encoding="utf8") as kaydet:
    #    for deger in eslesme:
    #         kaydet.write(deger.replace(".", ",") + "\n")    # "." nokta karakterini "," virgül ile değiştir, sonra kaydet.
#################################################################################################################################
