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

# DİKKAT: Aşağıdaki gibi bir "while 1 == 1" döngüsünün durma koşulu yoktur,
# yani sonsuza kadar çalışır (Infinite loop / Sonsuz Döngü) ve programı kilitler.
# Bu yüzden örnek olarak yorum satırına alındı, çalıştırmak isterseniz başındaki # işaretini kaldırın:
# while 1 == 1:
#     print('test')

"""
Geçen sefer yaptığımızdan daha gelişmiş bir hesap makinesi örneği aşağıda:
Bu sefer işlemi seçmekle kalmıyor, sayıları da alıp sonucu gerçekten hesaplıyoruz.
"""

# Kullanıcı "5" (Çıkış) seçene kadar menüyü tekrar tekrar gösterelim.
while True:
    print("---------------------------")
    print("Gelismis Hesap Makinesi")
    print(" ")
    print("Hangi islemi yapmak istersiniz?")
    print(" ")
    print("1) Toplama")
    print("2) Cikarma")
    print("3) Carpma")
    print("4) Bolme")
    print("5) Cikis")
    print("---------------------------")
    islem = input("> ")

    # Çıkış seçeneği ile döngüyü (ve programı) sonlandırıyoruz.
    if islem == "5":
        print("Gorusuruz!")
        break

    # Geçersiz bir seçenekte sayıları sormadan başa dönelim.
    if islem not in ("1", "2", "3", "4"):
        print("Gecersiz bir secenek belirttiniz.")
        continue

    # Seçilen işlem geçerliyse iki sayıyı alıp float'a çeviriyoruz (ondalıklı sayılar da çalışsın diye).
    sayi1 = float(input("1. sayi: "))
    sayi2 = float(input("2. sayi: "))

    if islem == "1":
        print("Sonuc: " + str(sayi1 + sayi2))
    elif islem == "2":
        print("Sonuc: " + str(sayi1 - sayi2))
    elif islem == "3":
        print("Sonuc: " + str(sayi1 * sayi2))
    elif islem == "4":
        # Bir sayıyı 0'a bölemeyiz, bu yüzden önce kontrol ediyoruz.
        if sayi2 == 0:
            print("Hata: Bir sayi 0'a bolunemez.")
        else:
            print("Sonuc: " + str(sayi1 / sayi2))
