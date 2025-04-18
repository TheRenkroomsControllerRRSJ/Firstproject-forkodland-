import time
meme_dict = {
        "CRINGE": "Garip ya da utandırıcı bir şey",
        "LOL": "Komik bir şeye verilen cevap",
        "ROFL": "bir şakaya karşılık cevap",
        "SHEESH": "onaylamamak",
        "CREEPY": "korkunç",
        "AGGRO": "agresifleşmek/sinirlenmek",
        ":D": "gülen yüz",
        ":)": "mutlu",
        ":(": "üzgün",
        ";(": "ağlıyor/ağlamak"
            }
print("EMOJI VE MODERN SÖZLÜĞE HOŞGELDİNİZ!")
time.sleep(1)
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!)(emojileri doğru şekilde yazınız): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("böyle bir kelime yok")
