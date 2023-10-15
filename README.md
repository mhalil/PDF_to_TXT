# PDF_to_TXT

PDF'ten TXT'ye dönüşüm ve Veri Madenciliği

Örnek **Analiz_Rapor.pdf** dosyası içindeki veriler [PyPDF2](https://github.com/py-pdf/pypdf) kütüphanesi yardımıyla **pdf_verisi.txt** dosyasına aktarıyoruz.

Ardından [RE (Regular Expression (Düzenli İfadeler))](https://docs.python.org/3/library/re.html) kütüphanesi yardımıyla, aranan değerlere (desenlere) uygun çıktıları elde ederek konsola yazdırıyor ya da **Rapor_Degerleri.txt** isimli dosyaya kaydediyoruz.



<u>Örnek desenler</u>;

```python
desen_brinell_sertlik = r"Brinell\s+\d+\.\d+\s+HBW"
desen_cekme_gerilmesi = r"\(Rm\)\s+\d+\.\d+\s+N/mm\^2\s+EN ISO 6892-1 Metod B"
desen_kimyasal = r"\*?\w+\s+<?\d+\.\d+\s+%\s+ASTM E1999"
```

<u>Örnek Çıkılar;</u>

```python
Brinell   195.10  HBW
Brinell   193.21  HBW
Brinell   190.44  HBW

(Rm)   562.00  N/mm^2  EN ISO 6892-1 Metod B
(Rm)   558.00  N/mm^2  EN ISO 6892-1 Metod B
(Rm)   552.00  N/mm^2  EN ISO 6892-1 Metod B

Ti  0.042  %  ASTM E1999
*Mg  0.040  %  ASTM E1999
C  3.688  %  ASTM E1999
Si  2.513  %  ASTM E1999
Mn  0.388  %  ASTM E1999
P  0.041  %  ASTM E1999
S  0.0069  %  ASTM E1999
Cr  0.017  %  ASTM E1999
Ni  <0.010  %  ASTM E1999
Cu  0.155  %  ASTM E1999
V  0.021  %  ASTM E1999
```
