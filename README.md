# 📄 **Energy Gym — Ma’lumot Beruvchi Chatbot**

Ushbu loyiha "Energy Gym" sport zali bo‘yicha barcha savollarga avtomatik tarzda javob beruvchi **AI chatbot**ni yaratish uchun ishlab chiqilgan. Bot sport zalining xizmatlari, tariflari, joylashuvi, ish vaqti, qo‘shimcha qulayliklari va boshqa ma’lumotlariga oid savollarga tez, aniq va kontekstga mos javob beradi.

Chatbot **OpenAI** va **LangChain** texnologiyalari orqali “Energy Gym”ga oid ma’lumotlar bazasini tahlil qilib, foydalanuvchilarga kerakli javobni shakllantiradi.

---
<img width="800" alt="image" src="https://github.com/user-attachments/assets/56defa0d-e5c9-4793-be40-ad7882d52f3e" />
<img width="800" alt="image" src="https://github.com/user-attachments/assets/becf4616-1fa0-47c6-b092-caa0301f1c95" />
<img width="800" alt="image" src="https://github.com/user-attachments/assets/3b288658-c19b-4510-b72c-c40fde6f467b" />

---

## 🔗 **Onlayn Loyiha Manzillari — “Sport zal menejeri”**

Quyidagi manzillar orqali loyihaning jonli versiyasidan foydalanishingiz mumkin:

* 💬 **Chat interfeys:**
  [https://zal.yourproject.uz/](https://zal.yourproject.uz/)

* 🧩 **API endpoint:**
  [https://zal.yourproject.uz/api/message/](https://zal.yourproject.uz/api/message/)

* 📘 **Swagger API Docs:**
  [https://zal.yourproject.uz/swagger/](https://zal.yourproject.uz/swagger/)

* 📕 **ReDoc API Docs:**
  [https://zal.yourproject.uz/redoc/](https://zal.yourproject.uz/redoc/)

---

## 🚀 **Texnologiyalar**

* **Python 3.11**
* **Django 5.1.4**
* **Django REST Framework 3.16.1**
* **OpenAI API (openai==0.28.0)**
* **LangChain >= 0.1.0**
* **PostgreSQL**
* **django-admin-interface**
* **django-ordered-model**
* **Whitenoise**
* **Gunicorn**
* **Requests**

---

## 🔧 **O‘rnatish bo‘yicha qo‘llanma**

### 1️⃣ Repository’ni klon qilish

```bash
git clone https://github.com/shamshod8052/RagChatbot
cd RagChatbot
```

---

### 2️⃣ Virtual environment yaratish

#### Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Kerakli paketlarni o‘rnatish

```bash
pip install -r requirements.txt
```

---

## 🔐 **Environment Variables ( `.env` )**

Loyiha to‘g‘ri ishlashi uchun `.env` fayliga quyidagi sozlamalarni kiriting:

```env
# django settings
SECRET_KEY=''
DEBUG=True
HOST=https://127.0.0.1

# openai settings
OPENAI_API_KEY=''

# postgresql info
DB_NAME=''
DB_USER=postgres
DB_PASS=''
DB_HOST=localhost
DB_PORT=5432
```

---

## ▶️ **Ishga tushirish**

Chatbotni va Django serverini ishga tushirish:

```bash
python manage.py runserver
```

---

## 📦 **Loyiha imkoniyatlari**

* 🧠 **AI asosidagi chatbot** — Energy Gym haqidagi barcha ma’lumotlarga kontekstli javoblar
* ⚙️ **RAG (Retrieval-Augmented Generation)** — LangChain bilan integratsiya qilingan aqlli javoblar
* 🗄 **PostgreSQL** — ma’lumotlar bazasi sifatida
* 🎛 **Admin Panel** — ma’lumotlarni boshqarish va kontent yangilash
* 🌐 **RESTful API** — tashqi xizmatlar bilan ulanish uchun
* 📄 **Swagger & ReDoc** — to‘liq API hujjatlari
* ☁️ **Gunicorn + Whitenoise** — production uchun tayyor server konfiguratsiyasi

---

## 📄 **Litsenziya**

MIT License

```
Copyright (c) 2025 Shamshod
```
