import json


def dosya_oku_ve_duzenle(kaynak_dosya_yolu, hedef_dosya_yolu):
    with open(kaynak_dosya_yolu, 'r', encoding='utf-8-sig') as kaynak_dosya:  
        veri = json.load(kaynak_dosya)  # JSON verisini oku

    girdiler = veri.get("input", [])
    output = veri.get("output", "Bu cümle 'Spor' kategorisine aittir.")  # Varsayılan değer

    yeni_formatli_veri = [{
        "instruction": "Aşağıdaki cümlenin Dünya, Ekonomi, Kültür, Sağlık, Spor, Teknoloji, Ürün Yorumu, Dizi-Film, Şikayet-Müşteri Geri Bildirim, Magazin kategorilerinden hangisine ait olduğunu söyle.",
        "input": girdi,
        "output": output
    } for girdi in girdiler]

    with open(hedef_dosya_yolu, 'w', encoding='utf-8') as hedef_dosya:
        json.dump(yeni_formatli_veri, hedef_dosya, indent=4, ensure_ascii=False)


kaynak_dosya_yolu = 'C:\\Users\\merte\\PycharmProjects\\NlpDataset\\nlpdataset.json'
hedef_dosya_yolu = 'C:\\Users\\merte\\PycharmProjects\\NlpDataset\\YeniDataset.json'
dosya_oku_ve_duzenle(kaynak_dosya_yolu, hedef_dosya_yolu)
