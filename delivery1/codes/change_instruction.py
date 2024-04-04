import json

with open('all_sağlık.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

for item in data:
    item['instruction'] = "Aşağıdaki cümlenin Dünya, Ekonomi, Kültür, Sağlık, Spor, Teknoloji, Ürün Yorumu, Dizi-Film, Şikayet-Müşteri Geri Bildirim, Magazin kategorilerinden hangisine ait olduğunu söyle."

with open('all_sağlık2.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)