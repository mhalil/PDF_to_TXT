import os, glob
from PyPDF2 import PdfReader

pdf_adi = input("PDF dosyasinin adini, uzantisiz olarak yazin: ")
dosya_adi = str(pdf_adi) + ".pdf"	# Dosya adı ve uzantisi

##### dosya adini al, veriyi kaydet #####
def pdf_dosya_adi():
	pdf_dosyasi = PdfReader(dosya_adi) # Dosya adı ve uzantisi
	toplam_safya_sayisi = len(pdf_dosyasi.pages)

	### Mevcut "pdf_verisi.txt" dosyasını sil
	txt_liste = glob.glob("*.txt")
	print(txt_liste)
	if "pdf_verisi.txt" in txt_liste:
		os.remove("pdf_verisi.txt")	
	################################################

	##### PDF Dosya içeriğini "pdf_verisi.txt" adıyla kaydeden Fonksiyon. ######
	def veriyi_kaydet():
		for sayfa in range(toplam_safya_sayisi):
			with open("pdf_verisi.txt", "a", encoding="utf8") as dosya: 
				dosya.write(pdf_dosyasi.pages[sayfa].extract_text())
	
	veriyi_kaydet()
################################################

##### pdf_to_txt() Fonksiyonunu Çalıştır. ######
pdf_dosya_adi()
################################################

##### pdf_verisi.txt dosyasını oku, belirtilen ifade ile biten satırları ekrana yazdır.
with open("pdf_verisi.txt", "r", encoding="utf-8") as dosya:
	icerik = dosya.readlines()
	# #print(icerik)
	gecici_numune_adi = ""
	gecici_analiz = ""
	for ic in icerik:
		if "Name, identity" in ic: 
			gecici_numune_adi = ic
		
		# #### Alternatif elif koşulu
		# #elif "Analiz" in ic or "ASTM E1999" in ic or "ASTM E1086" in ic or "EN ISO 6892-1 Metod B" in ic or "Brinell" in ic or "EN ISO 6506-1" in ic or "Shore A  TS ISO 48-2" in ic or "TS ISO 37" in ic:
		
		elif "Analiz" in ic:
			gecici_analiz = ic
			
		elif "%" in ic or "N/mm^2" in ic:
			# ## Sonucları Ekrana yazdır
			# #print(gecici_numune_adi[37:-1], "|", gecici_analiz[:-1], "|", ic[:-1], "|", ic.split("  ")[0].replace("*", ""), "|", ic.split("  ")[1].replace(".", ","), "\n")
						
			### sonucları "sonuc.tsv" adıyla kaydet
			with open(pdf_adi +".tsv", "a", encoding="utf-8") as sonuc:
				sonuc.write(gecici_numune_adi[37:-1] + "|" + gecici_analiz[:-1] + "|" + ic[:-1] + "|" + ic.split("  ")[0].replace("*", "") + "|" + ic.split("  ")[1].replace(".", ",") + "\n")
print("Ayıklanan test sonucları, 'sonuc.tsv' dosyasına kaydedildi")

# #################################################

