import json

# Okunacak ve yazılacak dosya yolları
input_file_path = r'C:\Users\90530\PycharmProjects\pythonVeriCekme\turkish-nlp-suite\beyazperde-top-300-movie-reviews.json'
output_file_path = r'C:\Users\90530\PycharmProjects\pythonVeriCekme\turkish-nlp-suite\beyazperde-top-300-movie-reviews2.json'



# Orijinal JSON dosyasını okur
with open(input_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Sadece "sentence" anahtarını içeren yeni bir sözlük oluşturur
new_data = {
    "text": data.get("text", [])
}

# Yeni veriyi yeni bir JSON dosyasına yazar
with open(output_file_path, 'w', encoding='utf-8') as file:
    json.dump(new_data, file, ensure_ascii=False, indent=4)

print(f"İşlem tamamlandı. Yeni dosya '{output_file_path}' olarak kaydedildi.")


