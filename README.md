# Python Dersleri

Bu depo, YouTube kanalımdaki Python eğitim serisinde yazdığım kodları içeriyor. Videoları izlerken buradaki dosyalara bakabilir, kendi bilgisayarınızda çalıştırıp üzerinde oynayabilirsiniz.

Oynatma listesi: [Python Eğitimi](https://www.youtube.com/playlist?list=PLi2glt6IPZ0UxXtsUj2h4CWuE8b-xobbG)

Her dersin kodu kendi klasöründe (`ders-1`, `ders-2`, ...) ve `uygulama.py` adıyla duruyor. Dosyaların içindeki yorum satırlarında konuyu adım adım anlatmaya çalıştım.

## Dersler

| Konu | Video | Kod |
| :--- | :--- | :--- |
| 1. Python Kurulumu ve İlk Program | [Video](https://www.youtube.com/watch?v=EGTltANA2hM) | [ders-1](./ders-1) |
| 2. Veri Türleri ve Değişkenler | [Video](https://www.youtube.com/watch?v=net3QeQqO1g) | [ders-2](./ders-2) |
| 3. Veri Dönüşümleri ve Girdiler | [Video](https://www.youtube.com/watch?v=5CP1KR7YOcA) | [ders-3](./ders-3) |
| 4. Koşullandırma ve Fonksiyonlar | [Video](https://www.youtube.com/watch?v=gUZ7K6XO0Rk) | [ders-4](./ders-4) |
| 5. Döngüler ve Modüller | [Video](https://www.youtube.com/watch?v=q9mF3PWz2h8) | [ders-5](./ders-5) |
| 6. Dosya İşlemleri | [Video](https://www.youtube.com/watch?v=UY_Zfq4_oKU) | [ders-6](./ders-6) |
| 7. Hata Yakalama | [Video](https://www.youtube.com/watch?v=N-og_lE0eFg) | [ders-7](./ders-7) |
| 8. Sınıflar | [Video](https://www.youtube.com/watch?v=OogXojwoCdc) | [ders-8](./ders-8) |

## Uygulamalar

Derslerin dışında birkaç küçük proje de var:

- **GUI örneği** — tkinter ile basit bir pencere: [kod](./gui-ornegi) · [video](https://www.youtube.com/watch?v=3eHQhwWyfro)
- **Chatbot** — sorulara benzer sorulardan cevap bulan, bilmediğini öğrenebilen basit bir bot: [kod](./yapay-zeka-ai-ornegi) · [video](https://www.youtube.com/watch?v=R8rrR2T9UX8)
- **Keylogger** — eğitim amaçlı tuş kaydı örneği: [kod](./keylogger-ornegi) · [video](https://www.youtube.com/watch?v=TW4USC9ZopQ)

Yalnızca videosu olan, bu depoda kodu bulunmayan diğer konular:

- [QR kod oluşturma](https://www.youtube.com/watch?v=p5ka7CsZxJ0)
- [NumPy kullanımı](https://www.youtube.com/watch?v=VyUj3nq0ZZc)
- [pyenv ile birden fazla Python sürümü](https://www.youtube.com/watch?v=WZMjsdJqiKQ)

## Çalıştırmak için

Python 3.10 veya üstü gerekiyor. Kurulu olup olmadığını şöyle kontrol edebilirsiniz:

```shell
python --version
```

Kurulu değilse [python.org](https://python.org) üzerinden indirin. Windows'ta kurulum sırasında **"Add Python to PATH"** kutusunu işaretlemeyi unutmayın.

Depoyu indirip bir dersi çalıştırmak:

```shell
git clone https://github.com/dincertekin/youtube-python-dersleri.git
cd youtube-python-dersleri
python ders-2/uygulama.py
```

GUI örneği için ek bir şey gerekmez, tkinter Python ile birlikte gelir.

## Katkı

Bir hata görürseniz ya da bir örneği iyileştirmek isterseniz issue açabilir veya pull request gönderebilirsiniz.

## Lisans

MIT. Ayrıntılar için [LICENSE](./LICENSE) dosyasına bakın.
