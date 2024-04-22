import os
import json

# Metin dosyalarının bulunduğu klasörün yolu
metin_klasor_yolu = "magazin"

tum_cumleler = []

# Metin klasöründeki her bir dosyayı işler
for dosya_adı in os.listdir(metin_klasor_yolu):
    dosya_yolu = os.path.join(metin_klasor_yolu, dosya_adı)
    if os.path.isfile(dosya_yolu) and dosya_adı.endswith(".txt"):
        with open(dosya_yolu, "r", encoding="utf-8") as dosya:
            icerik = dosya.read().replace("\n", " ")  # Alt satıra geçmeyi kaldırır

            cumleler = icerik.split(". ")

            # Her cümleyi birleştirerek tek bir cümle haline getirir
            birlesik_cümle = " ".join(cumleler)

            tum_cumleler.append(birlesik_cümle.strip())

# Toplanan cümleleri JSON dosyasına yazar
with open("toplanmis_cumleler-magazin.json", "w", encoding="utf-8") as dosya:
    json.dump(tum_cumleler, dosya, ensure_ascii=False, indent=4)