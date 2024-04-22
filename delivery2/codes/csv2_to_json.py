import csv
import json

def csv_to_json(csv_file, json_file):
    data = []
   
    with open(csv_file, 'r', encoding='utf-8-sig') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            data.append(row)

    with open(json_file, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(json.dumps(data, ensure_ascii=False, indent=4))

csv_to_json('input.csv', 'output.json')
