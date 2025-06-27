from flask import Flask
import random
app = Flask(__name__)
facts_list = [
    "Teknolojik bağımlılıktan mustarip olan kişiler cihazlarını kullanamayınca yoğun stres yaşarlar.",
    "18-34 yaş grubunun %50'sinden fazlası kendini akıllı telefon bağımlısı olarak görüyor.",
    "İnsanların %60'ı işten çıktıktan sonraki 15 dakika içinde iş mesajlarına yanıt veriyor.",
    "Teknolojik bağımlılıkla başa çıkmak için ruh halini iyileştiren etkinlikler bulun!",
    "Elon Musk, sosyal ağların bizi içeride tutmak için tasarlandığını söylüyor.",
    "Sosyal ağlar hem iyi hem de kötü yönler taşır. Bu yüzden dikkatli kullanmak gerekir."
]
@app.route("/")
def home():
    # Ana sayfada bir link gösteriyoruz
    return '''
        <h1>Ana Sayfa</h1>
        <p>Hoş geldin! Rastgele teknoloji gerçeği görmek için aşağıdaki linke tıkla:</p>
        <a href="/rastgele_gercek">Rastgele bir gerçeği görüntüle!</a>
    '''

@app.route("/rastgele_gercek")
def rastgele_gercek():
    # facts_list'ten rastgele bir gerçek seçip gösteriyoruz
    rastgele = random.choice(facts_list)
    return f'''
        <h1>Rastgele Gerçek</h1>
        <p>{rastgele}</p>
        <a href="/">Ana sayfaya dön</a>
    '''
if __name__ == "__main__":
    app.run(debug=True)
