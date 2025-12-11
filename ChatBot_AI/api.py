from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from translit import latin_to_cyr

# Model va index ni yuklaymiz
print("Model yuklanmoqda.......")
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Index yuklanmoqda......")
index = faiss.read_index("faiss_index.faiss")
answers = np.load("answers.npy", allow_pickle=True)

app = FastAPI(title="Uz Census Chatbot API")

class Question(BaseModel):
    question: str

def ask_bot(question):
    q_cyr = latin_to_cyr(question)
    emb = model.encode([q_cyr])
    D, I = index.search(emb, 1)
    return answers[I[0][0]]

@app.post("/ask")
def ask(q: Question):
    answer = ask_bot(q.question)
    return {"answer": answer}
