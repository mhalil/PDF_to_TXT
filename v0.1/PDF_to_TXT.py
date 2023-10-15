from PyPDF2 import PdfReader

pdf_dosya_adi = "Analiz_Rapor"
pdf_icerigi = PdfReader(pdf_dosya_adi + ".pdf")
toplam_safya_sayisi = len(pdf_icerigi.pages)

################################################################
##### PDF Dosya içeriğini "pdf_verisi.txt" adıyla kaydet. ######

for sayfa in range(toplam_safya_sayisi):
    with open("pdf_verisi.txt", "a", encoding="utf8") as dosya: 
        dosya.write(pdf_icerigi.pages[sayfa].extract_text())

################################################################
