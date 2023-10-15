import re


##### Çekme Deneyi - Akma Dayanımı (Rp0,2) Sonucu Deseni #############################################################################
desen_akma_dayanimi = r"Rp0,2\s+\d+\.\d+\s+N/mm\^2\s+EN ISO 6892-1 Metod B"  # Örnek eslesme: "Rp0,2  370.00  N/mm^2  EN ISO 6892-1 Metod B" - "\w+\d+,\d\s+\d+\.\d+\s+N/mm\^2\s+EN ISO 6892-1 Metod B" bu desen de olur.
################################################################################################################################

##### "pdf_verisi.txt" isimli dosya içeriğini oku, desen ile eşleşen değerleri Konsola yazdır. ####
def yazdir():
    with open("pdf_verisi.txt", "r", encoding="utf8") as dosya:
        icerik = dosya.read()
        eslesme = re.findall(desen_akma_dayanimi, icerik)
        for deger in eslesme:
            print("ÇEKME DENEYİ _ AKMA DAYANIMI - " + deger)      # esleşen değerleri alt alta yazdır, ekrana bas.  
#################################################################################################################################

##### "pdf_verisi.txt" isimli dosya içeriğini oku, desen ile eşleşen değerleri "Rapor_Degerleri.txt" isimli dosyaya ekle / kaydet. ####
def kaydet():
    with open("pdf_verisi.txt", "r", encoding="utf8") as dosya:
        icerik = dosya.read()
        eslesme = re.findall(desen_akma_dayanimi, icerik)
        with open("Rapor_Degerleri.txt", "a", encoding="utf8") as kaydet:
            for deger in eslesme:
                kaydet.write("ÇEKME DENEYİ _ AKMA DAYANIMI - " + deger.replace(".", ",") + "\n")    # "." nokta karakterini "," virgül ile değiştir, sonra kaydet.
########################################################################################################################################