print('Dosya okunuyor...')
# Dosyayı okumak için open fonksiyonunu 'r' parametresi (Read) ile vermemiz yeterlidir.
dosya = open("test.txt", 'r', encoding="utf-8")
okundu = dosya.read()
print(okundu)

# Aşağıdaki örnekte ise kullanıcının ismini alıp bir dosyaya yazıyoruz. 'w' (Write) dosyanın üzerine yazar, içeriği düşünmez! 
isim = input('Isminiz nedir? ')
dosya = open("test.txt", 'w', encoding="utf-8")
dosya.write(isim)
print('Dosyaya isim yazdirildi...')

# Soyismi yanına koymak istersek diye şöyle bir kod hazırladım, 'a' (Append) dosyanın var-olan halini bozmadan istediğinizi ekler.
soyisim = input('Soyisminiz nedir? ')
dosya = open("test.txt", 'a', encoding="utf-8")
dosya.write(' '+soyisim)
print('Dosyaya soyisim yazdirildi.')
