# İnsan diye bir sınıf oluşturduk, isim ve yaş parametrelerini alıyor.
class Insan:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas

# ornekKisi değişkenine İnsan sınıfından bir nesne oluşturduk, isim ve yaş kısmına Dinçer 21 verdik.
ornekKisi = Insan("Dinçer", 21)
print(ornekKisi.isim)

# Aşağıda ise bir örnek ATM sınıfı mevcut.
class ATM:
    def paraYatir(self, hesapNo, aciklama, tutar):
        print("Para yatirma islemi gerceklesti.")
    
    def paraCek(self, hesapNo, tutar):
        print("Para cekme islemi gerceklesti.")

ATM.paraYatir()
