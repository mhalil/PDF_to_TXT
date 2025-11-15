import re

##### Brinell_Sertlik Test Sonucu Deseni ##################################################################################
desen_brinell_sertlik = r"Brinell\s+\d+\.\d+\s+HBW"      # Örnek eslesme: "Brinell   195.10  HBW 2,5/187,5  EN ISO 6506-1"
###########################################################################################################################

##### "pdf_verisi.txt" isimli dosya içeriğini oku, desen ile eşleşen değerleri Konsola yazdır. ####
def yazdir():
    with open("pdf_verisi.txt", "r", encoding="utf8") as dosya:
        icerik = dosya.read()
        eslesme = re.findall(desen_brinell_sertlik, icerik)
        for deger in eslesme:
            print("BRINELL SERTLIK - " + deger.replace(".", ","))      # esleşen değerleri alt alta yazdır, ekrana bas.
#####################################################################################################

##### "pdf_verisi.txt" isimli dosya içeriğini oku, desen ile eşleşen değerleri "Rapor_Degerleri.txt" isimli dosyaya ekle / kaydet. ####
def kaydet():    
    with open("pdf_verisi.txt", "r", encoding="utf8") as dosya:
        icerik = dosya.read()
        eslesme = re.findall(desen_brinell_sertlik, icerik)
        with open("Rapor_Degerleri.txt", "a", encoding="utf8") as kaydet:
            for deger in eslesme:
                kaydet.write("BRINELL SERTLIK - " + deger.replace(".", ",") + "\n")    # "." nokta karakterini "," virgül ile değiştir, sonra kaydet.
##########################################################################################################################################