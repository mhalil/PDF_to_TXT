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

##### CONTA NUMUNESİ - Uzama Sonucu Deseni ############################################################
desen_conta_uzama = r"\*\w+\s+\d+\.\d+\s+N/mm\^2  TS ISO 37"  # Örnek eslesme: "*Uzama  371.00  N/mm^2  TS ISO 37"
##################################################################################################################

##### "pdf_verisi.txt" isimli dosya içeriğini oku, desen ile eşleşen değerleri "Brinell_Sertlik.txt" isimli dosyaya kaydet. ####
with open("pdf_verisi.txt", "r", encoding="utf8") as dosya:
    icerik = dosya.read()
    eslesme = re.findall(desen_conta_uzama, icerik)

    for deger in eslesme:
        print(deger)      # esleşen değerleri alt alta yazdır, ekrana bas.

    # with open("Conta_Uzama.txt", "w", encoding="utf8") as kaydet:
    #    for deger in eslesme:
    #         kaydet.write(deger.replace(".", ",") + "\n")    # "." nokta karakterini "," virgül ile değiştir, sonra kaydet.
#################################################################################################################################
