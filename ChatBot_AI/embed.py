# bu asosiy qisim embed.py fayli bo'lib, u ikkala script uchun ham embeddinglarni yaratadi va indeklaydi
import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from translit_embdy import   latin_to_cyrillic, cyrillic_to_latin
import os

print("Model yuklanmoqda...")
model = SentenceTransformer("all-MiniLM-L6-v2")

print("data.json o'qilmoqda... kuting ")
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

texts = []
answers = []
meta = []

for item in data:
    q = item["question"].strip()
    a = item["answer"].strip()
    texts.append(q)
    answers.append(a)
    meta.append({"id": item["id"], "orig": q})

    # Agar savol kirillcha bo'lsa — translit variantini ham qo'shamiz 
    # biz oddiy tekshiruv qilamiz: agar matnda kyrilcha harflar bo'lsa — demak u kirillcha deb hisoblaymiz 
    if re := any('\u0400' <= ch <= '\u04FF' for ch in q):
        lat = cyrillic_to_latin(q)
        texts.append(lat)
        answers.append(a)
        meta.append({"id": item["id"], "orig": q, "translit": lat})
    else:
        # agar lotincha bo'lsa — kirill variantini qo'shamiz
        cyr = latin_to_cyrillic(q)
        texts.append(cyr)
        answers.append(a)
        meta.append({"id": item["id"], "orig": q, "translit": cyr})

# Embedding va index
print("Embeddinglar yaratilmoqda...")
embeddings = model.encode(texts, show_progress_bar=True, convert_to_numpy=True)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
print("FAISS indexga qo'shilmoqda...")
index.add(embeddings)

# Saqlash
print("Fayllar saqlanmoqda...")
faiss.write_index(index, "faiss_index.faiss")
np.save("answers.npy", np.array(answers))
np.save("meta.npy", np.array(meta, allow_pickle=True))

print("Tayyor! Embeddings yaratildi va ikki script uchun ham indeklash amalga oshirildi.")
