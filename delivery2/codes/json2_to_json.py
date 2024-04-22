import json

def convert_to_json(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        data = json.load(infile)

    output_data = []
    for sentence in data:
        output_data.append({
            "instruction": "Aşağıdaki cümlenin Dünya, Ekonomi, Kültür, Sağlık, Spor, Teknoloji, Ürün Yorumu, Dizi-Film, Şikayet-Müşteri Geri Bildirim, Magazin, Kitap kategorilerinden hangisine ait olduğunu söyle.",
            "input": sentence.strip(),
            "output": "Bu cümle 'Kitap' kategorisine aittir."
        })

    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(output_data, outfile, ensure_ascii=False, indent=4)

convert_to_json('split_explanations.json', 'deneme_bakalim.json')