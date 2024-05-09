from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

reference = ['Dizi-Film']
candidate = ['Dizi-Film']

# BLEU skoru hesapla
bleu_score = sentence_bleu([reference], candidate, smoothing_function=SmoothingFunction().method1)

print("BLEU Score:", bleu_score)
