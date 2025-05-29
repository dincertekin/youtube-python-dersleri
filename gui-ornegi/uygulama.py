import tkinter as tk

# Pencere nesnemizi oluşturalım.
pencere = tk.Tk()

# Label oluşturalım ve bunu selam ismini verdiğimiz değişkenimize atayalım.
# İçerisinde Merhaba Dunya! yazsın ve yazı rengi yeşil arkaplanı sarı olsun.
selam = tk.Label(text="Merhaba Dunya!", fg="#00FF00", bg="yellow")
selam.pack()
# .pack() Paketleme fonksiyonumuz bir şeyi ekrana eklemeden önce paketlemeyi unutmayalım.

# Bana tikla! yazılı 100x30 bir buton örneği.
butonOrnegi = tk.Button(text="Bana tikla!", width=100, height=30)
butonOrnegi.pack()

# Ana döngüyü koymazsak penceremiz çalışmaz.
pencere.mainloop()
