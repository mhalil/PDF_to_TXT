import re

##### CONTA NUMUNESİ - Kopma Mukavemeti Sonucu Deseni ########################################################################################
desen_conta_kopma_mukavemeti = r"\*\w+\s+\w+\s+\d+\.\d+\s+N/mm\^2  TS ISO 37"  # Örnek eslesme: "*Kopma Mukavemeti   12.00  N/mm^2  TS ISO 37"
###############################################################################################################################################

##### "pdf_verisi.txt" isimli dosya içeriğini oku, desen ile eşleşen değerleri Konsola yazdır. ####
def yazdir():
    with open("pdf_verisi.txt", "r", encoding="utf8") as dosya:
        icerik = dosya.read()
        eslesme = re.findall(desen_conta_kopma_mukavemeti, icerik)
        for deger in eslesme:
            print("CONTA NUMUNESİ - " + deger)      # esleşen değerleri alt alta yazdır, ekrana bas.
#####################################################################################################

##### "pdf_verisi.txt" isimli dosya içeriğini oku, desen ile eşleşen değerleri "Rapor_Degerleri.txt" isimli dosyaya ekle / kaydet. #################
def kaydet():
    with open("pdf_verisi.txt", "r", encoding="utf8") as dosya:
        icerik = dosya.read()
        eslesme = re.findall(desen_conta_kopma_mukavemeti, icerik)
        with open("Rapor_Degerleri.txt", "a", encoding="utf8") as kaydet:
            for deger in eslesme:
                kaydet.write("CONTA NUMUNESİ - " + deger.replace(".", ",") + "\n")    # "." nokta karakterini "," virgül ile değiştir, sonra kaydet.
#####################################################################################################################################################