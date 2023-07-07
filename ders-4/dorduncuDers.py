# if: eğer
# else: değilse

def yasKontrol(isim: str, yas: int):
    if yas > 0 and yas < 13:
        print(isim+", bu filmi izlemek icin yasiniz 13'den buyuk olmali.")
    elif yas <= 0:
        print(isim+", hatali deger girdiniz.")
    else:
        print(isim+", bu filmi izleyebilirsiniz.")

kisininYasi = input("Yasiniz kactir? ")
yasKontrol("Dinçer", int(kisininYasi))
