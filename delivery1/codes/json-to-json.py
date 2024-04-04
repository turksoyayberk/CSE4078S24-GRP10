#Bu kod json dosyasında bir input altında birsürü veri olan şekildeki json dosyasını farklı inputlar içerisinde yazmayı sağlar.
#6,16,18,24. satırları değiştirerek kodu kullanabilirsiniz.
import json

# Giriş verisini oku
with open('müsteri-sikayet.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Yeni veriyi saklamak için boş bir liste oluştur
new_entries = []

# Her bir giriş için işlem yap
for entry in data['input']:
    # Yeni instruction ve output oluştur
    new_entry = {
        "instruction": "Aşağıdaki cümlenin hangi kategoride bulunduğunu söyle.",
        "input": entry,
        "output": "Bu cümle 'Şikayet-Müşteri Geri Bildirim' kategorisine aittir."
    }
    # Yeni girişi listeye ekle
    new_entries.append(new_entry)

# Yeni veriyi yaz
with open('output_sikayet.json', 'w', encoding='utf-8') as output_file:
    json.dump(new_entries, output_file, ensure_ascii=False, indent=4)
