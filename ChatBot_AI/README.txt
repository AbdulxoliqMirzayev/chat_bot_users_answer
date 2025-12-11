====================================================
        UZB CENSUS CHATBOT — INSTALLATION GUIDE
====================================================

Ushbu loyiha foydalanuvchilardan olingan savollarga 
javob beruvchi AI chatbot API xizmatidir. 

Chatbot lotin va kirill yozuvida berilgan savollarni 
tanib oladi va mos javobni qaytaradi.

----------------------------------------------------
1. SISTEMA TALABLARI
----------------------------------------------------

Serveringizda quyidagi dasturlar bo‘lishi kerak:

- Python 3.10 yoki 3.11
- Pip (python paket menejeri)
- Git (ixtiyoriy)
- 2 GB RAM minimal (tavsiya qilinadi)

----------------------------------------------------
2. LOYIHANI YUKLASH
----------------------------------------------------

ChatBot_AI papkasini serverga yuklang.

Masalan:

/home/username/ChatBot_AI/

Papka ichida quyidagi fayllar bo‘lishi kerak:

- api.py
- embed.py
- query.py
- translit.py
- data.json
- faiss_index.faiss
- answers.npy
- requirements.txt
- README.txt  (shu fayl)

----------------------------------------------------
3. VIRTUAL MUHIT YARATISH
----------------------------------------------------

Terminalda loyiha papkasiga kiring:

cd ChatBot_AI

Virtual environment yaratish:

python3 -m venv venv

Aktivlashtirish:

source venv/bin/activate

(Windows bo‘lsa)
venv\Scripts\activate

----------------------------------------------------
4. KUTUBXONALARNI O‘RNATISH
----------------------------------------------------

pip install -r requirements.txt

Agar o‘rnatishda xatolik bo‘lsa:

pip install --upgrade pip

----------------------------------------------------
5. EMBEDDING YARATISH (faqat bir marta)
----------------------------------------------------

Bu bosqich data.json dagi savol-javoblarni 
AI modeliga tayyorlab beradi.

Bajarish:

python embed.py

Ushbu fayllar yangilanadi:
- faiss_index.faiss
- answers.npy

----------------------------------------------------
6. API SERVERNI ISHGA TUSHIRISH
----------------------------------------------------

Quyidagi buyruq bilan API ni ishga tushirasiz:

uvicorn api:app --host 0.0.0.0 --port 8000

Agar server fon rejimida ishlashi kerak bo‘lsa:

nohup uvicorn api:app --host 0.0.0.0 --port 8000 &

API hozir mana bu manzilda ishlaydi:

http://YOUR_SERVER_IP:8000/ask

----------------------------------------------------
7. APIga QANDAY MUROJAAT QILISH (WEBSITE, BOT VA H.K.)
----------------------------------------------------

POST so‘rov yuboring:

URL:
http://YOUR_SERVER_IP:8000/ask

Body (JSON):

{
    "question": "uy hojaligiga kimlar kiradi"
}

Javob:

{
    "answer": "Уй хўжалиги - битта турар жойда..."
}

----------------------------------------------------
8. TEST QILISH (BRAUZER ORQALI)
----------------------------------------------------

Brauzerga kirib yozing:

http://YOUR_SERVER_IP:8000/docs

Bu yerda API ni real vaqt rejimida test qilishingiz mumkin.

----------------------------------------------------
9. SERVERNI QAYTA ISHLATISH
----------------------------------------------------

Agar server o‘chib qolsa, API ni qayta yoqing:

source venv/bin/activate
uvicorn api:app --host 0.0.0.0 --port 8000

----------------------------------------------------
10. MUAMMOLAR BO‘LSA
----------------------------------------------------

1) Pip xatolik chiqarsa:
   pip install --upgrade pip

2) Model yuklanmasa:
   Internet ishlayotganini tekshiring.

3) “Module not found” bo‘lsa:
   venv aktivlanganligiga ishonch hosil qiling.

----------------------------------------------------
CHATBOT TAYYOR!

Endi siz API URL-ni web sahifangizga ulashingiz mumkin.
====================================================
