# Gradio interfeys uchun kod
import gradio as gr
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from translit import latin_to_cyr

# Model va indexni yuklaymiz
print("Model yuklanmoqda............")
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Index yuklanmoqda..........")
index = faiss.read_index("faiss_index.faiss")
answers = np.load("answers.npy", allow_pickle=True)


def ask_bot(message, chat_history):
    try:
        if chat_history is None:
            chat_history = []

        #  Lotincha savolni kirillga o‘tkazamiz
        message_cyr = latin_to_cyr(message)

        q_emb = model.encode([message_cyr])
        D, I = index.search(q_emb, 1)
        answer = answers[I[0][0]]

        chat_history.append({"role": "user", "content": message})
        chat_history.append({"role": "assistant", "content": answer})

        
        return chat_history, chat_history

    except Exception as e:
        err = f"Xatolik: {str(e)}"
        if chat_history is None:
            chat_history = []
        chat_history.append({"role": "user", "content": message})
        chat_history.append({"role": "assistant", "content": err})
        return chat_history, chat_history


# Gradio interfeys
with gr.Blocks(title="Uz Census Chatbot") as demo:
    gr.Markdown("<h2 style='text-align:center;'> Census Chatbot</h2>")

    chatbot = gr.Chatbot(value=[], elem_id="chatbot", label="Chat")
    with gr.Row():
        txt = gr.Textbox(show_label=False, placeholder="Savol yozing... (lotin yoki kirill bo'lishi mumkin)", lines=1)
        clear = gr.Button("Tozalash")

    # submit — funksiyaga (message, history) argumentlarini beradi
    txt.submit(ask_bot, [txt, chatbot], [chatbot, chatbot])
    clear.click(lambda: ([], []), None, [chatbot, chatbot])


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
