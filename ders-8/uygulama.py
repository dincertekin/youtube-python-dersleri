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

# Metotları çağırmak için önce sınıftan bir nesne oluşturmamız gerekiyor.
atmNesnesi = ATM()
# Ardından nesne üzerinden metodu, istediği parametrelerle çağırıyoruz.
# (self parametresini biz vermiyoruz, Python onu otomatik gönderir.)
atmNesnesi.paraYatir("12345", "Birikim", 500)
atmNesnesi.paraCek("12345", 200)
