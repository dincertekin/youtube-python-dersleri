# Döngüler, geçen ders söylediğimiz gibi fonksiyonlara benzer şekilde tekrarlayan işlemlerde kullanılır.
# Fakat bu sefer kodun tekrarlayacağı şeylerde kullanacağız bizim tekrar yazacağımız şeylerde değil.

# Örneğin 1'den 100'e kadar 1. Merhaba Dünya 2. Merhaba Dünya şeklinde yazsın istiyoruz.
for i in range(1, 101):
    # i adında verimiz aralıkta(1, 101) Neden mi 101? çünkü < 101 şeklinde işleyecek.
    print(str(i)+". Merhaba Dünya")

# Arabalar dizisi oluşturalım.
arabalar = [
    "Audi",
    "Mercedes",
    "BMW",
    "Tofaş",
    "Bilinmeyen"
]

# Arabalar dizisi içindeki her bir araba markasını ekrana yazdırmak istersek:
for arabaMarkasi in arabalar:
    print(arabaMarkasi)

# Infinite loop (Sonsuz Döngü) bunun sonu yok! Tehlikelidir.
while 1 == 1:
    print('test')

"""
Geçen sefer yaptığımızdan daha gelişmiş bir hesap makinesi örneği aşağıda:
"""

sonsuzDongu = 1
while sonsuzDongu == 1:
    print("---------------------------")
    print("Gelismis Hesap Makinesi")
    print(" ")
    print("Hangi islemi yapmak istersiniz?")
    print(" ")
    print("1) Toplama")
    print("2) Cikarma")
    print("3) Carpma")
    print("4) Bolme")
    print("---------------------------")
    islem = input("> ")
    if int(islem) == 1:
        print("Toplama islemini sectiniz, sayilari girin: ")
    elif int(islem) == 2:
        print("Cikarma islemini sectiniz, sayilari girin: ")
    elif int(islem) == 3:
        print("Carpma islemini sectiniz, sayilari girin: ")
    elif int(islem) == 4:
        print("Bolme islemini sectiniz, sayilari girin: ")
        sureklidongu = 0
    else:
        print('Gecersiz bir secenek belirttiniz.')
