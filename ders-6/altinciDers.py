# dosya açma
# dosya oluşturma
# dosyaya veri yazma
# dosyadan veri okuma

print('Dosya okunuyor...')
dosya = open("test.txt", 'r', encoding="utf-8")
okundu = dosya.read()
print(okundu)

isim = input('Isminiz nedir? ')
dosya = open("test.txt", 'w', encoding="utf-8")
dosya.write(isim)
print('Dosyaya isim yazdirildi...')

soyisim = input('Soyisminiz nedir? ')
dosya = open("test.txt", 'a', encoding="utf-8")
dosya.write(' '+soyisim)
print('Dosyaya soyisim yazdirildi.')
