import json
import pandas as pd

# JSON dosyasını aç ve içeriğini yükle
with open('Marmara-NLPCSE4078S24_Grp10_Test_Dataset(110)_Text_Classification.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# input ve output değerlerini listelere kaydet
inputs = [item['input'] for item in data]
outputs = [item['output'] for item in data]

# Listeleri DataFrame'e dönüştür
df = pd.DataFrame({
    'input': inputs,
    'output': outputs
})

# DataFrame'i Excel dosyasına kaydet
df.to_excel('excel.xlsx', index=False)
