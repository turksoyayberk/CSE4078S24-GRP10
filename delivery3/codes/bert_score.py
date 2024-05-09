from bert_score import score

reference = 'Bu cümle Ekonomi kategorisine aittir.'  # Tek bir metin
candidate = 'Bu cümle Spor kategorisine aittir.'   # Tek bir metin

# BERTScore hesapla
bert_score = score([candidate], [reference], lang="tr", model_type="dbmdz/bert-base-turkish-cased")

print("BERTScore:", bert_score[2].item())

