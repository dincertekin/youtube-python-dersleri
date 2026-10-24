print('Dosya okunuyor...')
# Dosyayı okumak için open fonksiyonunu 'r' parametresi (Read) ile açıyoruz.
# "with" bloğu kullanıyoruz; çünkü blok bittiğinde dosyayı otomatik olarak kapatır.
# (Dosyayı kapatmayı unutmak sık yapılan bir hatadır, with bunu bizim yerimize halleder.)
with open("test.txt", 'r', encoding="utf-8") as dosya:
    okundu = dosya.read()
print(okundu)

# Aşağıdaki örnekte ise kullanıcının ismini alıp bir dosyaya yazıyoruz. 'w' (Write) dosyanın üzerine yazar, içeriği düşünmez!
isim = input('Isminiz nedir? ')
with open("test.txt", 'w', encoding="utf-8") as dosya:
    dosya.write(isim)
print('Dosyaya isim yazdirildi...')

# Soyismi yanına koymak istersek diye şöyle bir kod hazırladım, 'a' (Append) dosyanın var-olan halini bozmadan istediğinizi ekler.
soyisim = input('Soyisminiz nedir? ')
with open("test.txt", 'a', encoding="utf-8") as dosya:
    dosya.write(' '+soyisim)
print('Dosyaya soyisim yazdirildi.')
