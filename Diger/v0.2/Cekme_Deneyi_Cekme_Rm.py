import re

##### Çekme Deneyi - Çekme Gerilmesi (Rm) Sonucu Deseni #############################################################################
desen_cekme_gerilmesi = r"\(Rm\)\s+\d+\.\d+\s+N/mm\^2\s+EN ISO 6892-1 Metod B"      # Örnek eslesme: "Çekme Gerilmesi (Rm)   562.00  N/mm^2  EN ISO 6892-1 Metod B" - "\(\w+\)\s+\d+\.\d+\s+N/mm\^2\s+EN ISO 6892-1 Metod B" bu deen de olur
################################################################################################################################

##### "pdf_verisi.txt" isimli dosya içeriğini oku, desen ile eşleşen değerleri Konsola yazdır. ####
def yazdir():
    with open("pdf_verisi.txt", "r", encoding="utf8") as dosya:
        icerik = dosya.read()
        eslesme = re.findall(desen_cekme_gerilmesi, icerik)
        for deger in eslesme:
            print("ÇEKME DENEYİ _ ÇEKME GERİLMESİ - " + deger)      # esleşen değerleri alt alta yazdır, ekrana bas.
#####################################################################################################

##### "pdf_verisi.txt" isimli dosya içeriğini oku, desen ile eşleşen değerleri "Rapor_Degerleri.txt" isimli dosyaya ekle / kaydet. ####
def kaydet():
    with open("pdf_verisi.txt", "r", encoding="utf8") as dosya:
        icerik = dosya.read()
        eslesme = re.findall(desen_cekme_gerilmesi, icerik)
        with open("Rapor_Degerleri.txt", "a", encoding="utf8") as kaydet:
            for deger in eslesme:
                kaydet.write("ÇEKME DENEYİ _ ÇEKME GERİLMESİ - " + deger.replace(".", ",") + "\n")    # "." nokta karakterini "," virgül ile değiştir, sonra kaydet.
#######################################################################################################################################