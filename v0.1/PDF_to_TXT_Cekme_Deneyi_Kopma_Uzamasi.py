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

##### Çekme Deneyi - Kopma Uzaması (A5) Sonucu Deseni #############################################################################
desen_kopma_uzamasi = r"A5\s+\d+\.\d+\s+%\s+EN ISO 6892-1 Metod B"  # Örnek eslesme: "A5  7.000  %  EN ISO 6892-1 Metod B"
################################################################################################################################

##### "pdf_verisi.txt" isimli dosya içeriğini oku, desen ile eşleşen değerleri "Brinell_Sertlik.txt" isimli dosyaya kaydet. ####
with open("pdf_verisi.txt", "r", encoding="utf8") as dosya:
    icerik = dosya.read()
    eslesme = re.findall(desen_kopma_uzamasi, icerik)

    for deger in eslesme:
        print(deger)      # esleşen değerleri alt alta yazdır, ekrana bas.

    # with open("Cekme_Deneyi_Kopma_Uzamasi.txt", "w", encoding="utf8") as kaydet:
    #    for deger in eslesme:
    #         kaydet.write(deger.replace(".", ",") + "\n")    # "." nokta karakterini "," virgül ile değiştir, sonra kaydet.
#################################################################################################################################
