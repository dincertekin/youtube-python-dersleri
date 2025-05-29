# Fonksiyonlar tekrarlayan işlerimizi hızlandırmak için kullanılır.
# Örneğin kodun birkaç kısmında yaş kontrolü yapacağız diyelim, 6 satırı tekrar tekrar kopyala-yapıştır mı yapalım?
# Gerek yok, fonksiyonlar hayatınızı kurtarabilir:

# Fonksiyonlar def ile belirtilir def'ten sonra gelen kısım fonksiyonun adıdır. Parantez içindekiler ise alacağı parametreler.
def yasKontrol(isim: str, yas: int):
    # if: eğer
    if yas > 0 and yas < 13:
        # eğer yaş 0'dan büyük ve yaş 13'ten de küçük ise:
        print(isim+", bu filmi izlemek icin yasiniz 13'den buyuk olmali.")
    # else: değilse
    elif yas <= 0:
        # yaş 0'dan küçük veya eşitse
        print(isim+", hatali deger girdiniz.")
    else:
        # diğer tüm olaylar için else koyduk.
        print(isim+", bu filmi izleyebilirsiniz.")

# Kişinin yaşını isteyeceğiz.
kisininYasi = input("Yasiniz kactir? ")
# Aldığımız veriyi Integer'a çevirip fonksiyonumuza iletiyoruz, gerisini o hallediyor.
yasKontrol("Dinçer", int(kisininYasi))
