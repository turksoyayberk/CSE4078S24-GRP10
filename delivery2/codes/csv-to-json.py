import csv
import json
import sys

#Bu kod dosyası .csv formatındaki datasetleri .json formatına çevirir.
#Kullanmak için 30.satırı düzenleyin.

# Alan sınırını artır
csv.field_size_limit(2147483647)

def csv_to_json(csv_file, json_file):
    # CSV dosyasını oku ve JSON dosyasına dönüştür
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        # CSV dosyasını oku
        csv_reader = csv.DictReader(file)
        
        # JSON formatında saklamak için boş bir liste oluştur
        data = []
        
        # Her satır için işlem yap
        for row in csv_reader:
            # Her satırı bir sözlüğe dönüştür
            data.append(row)
    
    # JSON dosyasına veriyi yaz
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# Örnek kullanım
csv_to_json('example1.csv', 'example2.json')
