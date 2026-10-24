# random: Rastgele sayılar üreteceğimiz için içe aktaralım.
import random

# Rastgele bir sayı oluşturup ekrana yazdırmak için:
rastgeleInteger = random.randint(5, 15)
print(rastgeleInteger)

deneme = random.randrange(12, 49)
print(deneme)

rastgeleInteger = random.randint(5, 15)
print(rastgeleInteger)

deneme = random.randrange(12, 49)
print(deneme)

# Meyveler dizisi oluşturalım.
meyveler = [
    'elma',
    'armut',
    'muz',
    'cilek'
]
# Rastgele bir meyve seçmesini istesek?
print(random.choice(meyveler))

# Hataları ağaçtan düşen elmayı yakalar gibi yakalayabiliriz, bakınız:
birString = "Deneme yazisi."
birSayi = 19
ikinciSayi = 249

# Hatayı yakalarsak eğer, kodun yürütülmesine engel olmadan istediğimiz yönü verebiliriz.
try:
    # Bir yazı (str) ile sayıyı (int) toplamaya çalışınca Python TypeError hatası verir.
    a = birString + birSayi + ikinciSayi
    print(a)
except TypeError:
    # Hata oluşursa program durmaz, bunun yerine buradaki mesaj çalışır.
    print('Bir yazi/sayi toplama sorunu var (TypeError).')
else:
    # else bloğu SADECE try içinde hiç hata olmazsa çalışır. Burada hata oluştuğu için çalışmayacak.
    print('Hic hata olmadi.')
finally:
    # finally bloğu hata olsa da olmasa da her durumda kesinlikle çalışır.
    print('Kesinlikle yurutulecek')

# Kendi hatamızı oluşturalım:
x = 5
if x < 6:
  raise Exception("Alti sayisinin altinda bir rakam veremezsin.")
