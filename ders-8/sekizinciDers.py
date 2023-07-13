# Sınıfları Tanıyalım
# Sınıf Tam Olarak Nedir?
# Örneklendirme

class Insan:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas

ornekKisi = Insan("Dinçer", 19)
print(ornekKisi.isim)

class Banka:
    def paraYatir(self, hesapNo, aciklama, tutar):
        print("Para yatirma islemi gerceklesti.")
    
    def paraCek(self, hesapNo, tutar):
        print("Para cekme islemi gerceklesti.")

Banka.paraYatir()
