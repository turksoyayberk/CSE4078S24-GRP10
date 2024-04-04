import json

# Orjinal JSON dosyasının adı
orjinal_dosya_adı = "2_YENI_TRT_Haber_Dünya.json"

# Yeni JSON dosyasının adı
yeni_dosya_adı = "Yeni_2_YENI_TRT_Haber_Dünya.json"

# Orjinal JSON dosyasını oku
with open(orjinal_dosya_adı, 'r', encoding='utf-8') as f:
    orjinal_veri = json.load(f)

# Yeni JSON dosyasına yazılacak veri
yeni_veri = [haber["Icerik"] for haber in orjinal_veri]

# Yeni JSON dosyasına yaz
with open(yeni_dosya_adı, 'w', encoding='utf-8') as f:
    json.dump(yeni_veri, f, ensure_ascii=False, indent=4)

print("Yeni JSON dosyası oluşturuldu:", yeni_dosya_adı)
