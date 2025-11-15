from PyPDF2 import PdfReader

##### dosya adini al, veriyi kaydet #####
def pdf_dosya_adi():
	pdf_dosya_adi = input("Dosya adini, uzantisiz olarak yazin: ")
	pdf_dosyasi = PdfReader(pdf_dosya_adi + ".pdf") # Dosya adı ve uzantisi
	toplam_safya_sayisi = len(pdf_dosyasi.pages)

	##### PDF Dosya içeriğini "pdf_verisi.txt" adıyla kaydeden Fonksiyon. ######
	def veriyi_kaydet():
		for sayfa in range(toplam_safya_sayisi):
			with open("pdf_verisi.txt", "a", encoding="utf8") as dosya: 
				dosya.write(pdf_dosyasi.pages[sayfa].extract_text())
	
	veriyi_kaydet()
############################################################################

##### pdf_to_txt() Fonksiyonunu Çalıştır. ######
# #pdf_dosya_adi()
################################################
