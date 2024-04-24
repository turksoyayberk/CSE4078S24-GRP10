import json
import statistics

def calculate_character_count(json_data):
    character_counts = []
    total_character_count = 0
    for item in json_data:
        if 'input' in item:
            character_count = len(item['input'])
            character_counts.append(character_count)
            total_character_count += character_count
    return character_counts, total_character_count

# JSON file
with open('CSE4078S24_Grp10_AlpacaStyle_DatasetCombined.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# calculate avg character
character_counts, total_character_count = calculate_character_count(data)

# count of ınput
input_data_count = len(data)

# calculate avg character
average_character_count = total_character_count / input_data_count

# calculate std. dev.
standard_deviation = statistics.stdev(character_counts)

# result
print("Toplam karakter sayısı:", total_character_count)
print("Input alanındaki karakter sayılarının ortalaması:", average_character_count)
print("Input alanındaki karakter sayılarının standart sapması:", standard_deviation)
