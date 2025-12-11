import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from translit import latin_to_cyr

print("Model yuklanmoqda...")
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Index yuklanmoqda...")
index = faiss.read_index("faiss_index.faiss")
answers = np.load("answers.npy", allow_pickle=True)

def ask_bot(question):
    #  Lotin hariflaarida  bo'lsa  avtomatik kirillga o‘tkazamiz
    q_cyr = latin_to_cyr(question)

    #  Embedding
    q_emb = model.encode([q_cyr])

    #  Qidiruv 
    D, I = index.search(q_emb, 1)

    # Eng yaqin javobni olish
    return answers[I[0][0]]

if __name__ == "__main__":
    print("Chatbot tayyor...!")
    while True:
        savol = input("Savol yozing : ")
        if savol in ["exit", "quit", "stop"]:
            break

        javob = ask_bot(savol)
        print("\nJavob :", javob, "\n")
