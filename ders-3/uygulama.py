# Ekrana Basit hesap makinesini yazdırdık.
print("Basit hesap makinesi")

# sayi1 ve sayi2 ismini verdiğimiz değişkenlere kullanıcıdan alacağımız veriyi verdik.
sayi1 = input("Toplama isleminde kullanilacak ilk sayi nedir? ")
sayi2 = input("Toplama isleminde kullanilacak ikinci sayi nedir? ")

# int() fonksiyonu yukarıda String (Metinsel veri) olan sayi1 ve sayi2'yi Integer (sayı veri tipine) dönüştürür.
# Integer'a dönüştürdükten sonra toplayabiliriz, iki metni nasıl toplayacaksınız hesap makinesinde? İki sayı toplanabilir :)
toplam = int(sayi1) + int(sayi2)

# Toplamlarını ekrana yazdırırken tekrar String'e (Metinsel veriye) dönüştürelim.
print("Toplamlari: " + str(toplam))
