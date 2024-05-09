import pandas as pd

# Excel dosyasını yükle
df = pd.read_excel('dosyanızın_yolu512512.xlsx')

# 'Fine-Tuned Model Output' sütunundaki '###' işaretlerini sil
df['Fine-Tuned Model Output'] = df['Fine-Tuned Model Output'].str.replace('### ', '', regex=False)

# Düzeltilmiş DataFrame'i yeni bir Excel dosyasına kaydet
df.to_excel('Mert_512_512.xlsx', index=False)
