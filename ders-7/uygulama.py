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
    a = birString + birSayi + ikinciSayi
    print(a)
except TypeError:
    print('Bir yazi sorunu var: Satir 10.')
else:
    print('Baska bir durum soz konusu.')
finally:
    print('Kesinlikle yurutulecek')

# Kendi hatamızı oluşturalım:
x = 5
if x < 6:
  raise Exception("Alti sayisinin altinda bir rakam veremezsin.")
