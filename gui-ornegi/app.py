import tkinter as tk

pencere = tk.Tk()

selam = tk.Label(text="Merhaba Dunya!", fg="#00FF00", bg="yellow")
selam.pack()

butonOrnegi = tk.Button(text="Bana tikla!", width=100, height=30)
butonOrnegi.pack()

pencere.mainloop()
