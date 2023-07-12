# Ice Aktaralim
import random
import datetime

# DateTime Modulu
rastgeleInteger = random.randint(5, 15)
print(rastgeleInteger)

deneme = random.randrange(12, 49)
print(deneme)

# Random Modulu
rastgeleInteger = random.randint(5, 15)
print(rastgeleInteger)

deneme = random.randrange(12, 49)
print(deneme)

meyveler = [
    'elma',
    'armut',
    'muz',
    'cilek'
]

print(random.choice(meyveler))

# Hata Yakalama
birString = "Deneme yazisi."
birSayi = 19
ikinciSayi = 249

try:
    a = birString + birSayi + ikinciSayi
    print(a)
except TypeError:
    print('orada bir yazi sorunu var. satir 10')
else:
    print('Baska bir durum soz konusu.')
finally:
    print('Kesinlikle yurutulecek')

x = 5
if x < 6:
  raise Exception("Alti sayisinin altinda bir rakam veremezsin.")
