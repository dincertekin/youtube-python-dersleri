# for nedir?
# while nedir?

# for ve while'ın farkı!

# nerede for kullanırız?
# nerede while kullanırız?

for i in range(1, 101):
    print(str(i)+". Merhaba Dünya")

arabalar = [
    "Audi",
    "Mercedes",
    "BMW",
    "Tofaş",
    "Bilinmeyen"
]

for arabaMarkasi in arabalar:
    print(arabaMarkasi)

while 1 == 1:
    print('test')

"""
DİĞER KISIM:
"""

sureklidongu = 1
while sureklidongu == 1:
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
