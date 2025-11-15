import re

##### Çekme Deneyi - Kopma Uzaması (A5) Sonucu Deseni #############################################################################
desen_kopma_uzamasi = r"A5\s+\d+\.\d+\s+%\s+EN ISO 6892-1 Metod B"  # Örnek eslesme: "A5  7.000  %  EN ISO 6892-1 Metod B"
################################################################################################################################

##### "pdf_verisi.txt" isimli dosya içeriğini oku, desen ile eşleşen değerleri Konsola yazdır. ####
def yazdir():
    with open("pdf_verisi.txt", "r", encoding="utf8") as dosya:
        icerik = dosya.read()
        eslesme = re.findall(desen_kopma_uzamasi, icerik)
        for deger in eslesme:
            print("ÇEKME DENEYİ _ KOPMA UZAMASI - " + deger)      # esleşen değerleri alt alta yazdır, ekrana bas.
#####################################################################################################

##### "pdf_verisi.txt" isimli dosya içeriğini oku, desen ile eşleşen değerleri "Rapor_Degerleri.txt" isimli dosyaya ekle / kaydet. ####
def kaydet():
    with open("pdf_verisi.txt", "r", encoding="utf8") as dosya:
        icerik = dosya.read()
        eslesme = re.findall(desen_kopma_uzamasi, icerik)
        with open("Rapor_Degerleri.txt", "a", encoding="utf8") as kaydet:
            for deger in eslesme:
                kaydet.write("ÇEKME DENEYİ _ KOPMA UZAMASI - " + deger.replace(".", ",") + "\n")    # "." nokta karakterini "," virgül ile değiştir, sonra kaydet.
#######################################################################################################################################