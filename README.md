# Yangiliklar Sayti

Bu loyiha oddiy yangiliklar saytini yaratish uchun ishlatiladi. Sayt foydalanuvchilarga yangiliklarni ko'rish va yangi yangiliklarni qo'shish imkoniyatini beradi.

## Loyiha Tuzilishi

- **Bosh Sahifa:** Saytning asosiy sahifasi. Barcha kategoriyalardagi yangiliklar ro'yxati ko'rsatiladi.
- **Kategoriyalar:**
  - Mahalliy
  - Jahon
  - Sport
  - Texnologiya
- **Yangilik Qo'shish:** Admin yoki ruxsat berilgan foydalanuvchilar yangilik qo'shishlari mumkin.

## Texnologiyalar

- **Frontend:** HTML, CSS (Bootstrap yoki o'zingiz tanlagan framework), JavaScript
- **Backend:** Django yoki Flask
- **Ma'lumotlar Bazasi:** SQLite (yoki boshqa kerakli DBMS)

## Loyihaning Ishlash Tizimi

1. Foydalanuvchi saytda mavjud bo'lgan kategoriyalarga o'tib, yangiliklarni ko'radi.
2. Texnologiya sahifasi kabi bo'sh bo'lgan sahifalarda "Hozircha yangiliklar mavjud emas" degan xabar chiqadi.
3. "Yangilik Qo'shish" sahifasi orqali yangilik qo'shish mumkin:
   - Sarlavha, kategoriya, qisqa tavsif va to'liq matnni kiritish talab qilinadi.

## Foydalanish Bo'yicha Yo'riqnoma

1. **Yangiliklarni Ko'rish:**

   - Saytning bosh sahifasiga o'tib, barcha kategoriyadagi yangiliklarni ko'rishingiz mumkin.
   - Ma'lum bir kategoriyaga o'tish uchun menyudan foydalaning.

2. **Yangilik Qo'shish:**

   - "Yangilik Qo'shish" tugmasi orqali kerakli formani to'ldiring:
     - **Sarlavha:** Yangilik nomi.
     - **Kategoriya:** Yangilik turi (Masalan: Texnologiya).
     - **Qisqa Tavsif:** Yangilikning qisqacha mazmuni.
     - **To'liq Matn:** To'liq ma'lumot.

## O'rnatish Yo'riqnomasi

1. **Kodni Yuklab Olish:**

   ```bash
   git clone https://github.com/username/yangiliklar-sayti.git
   cd yangiliklar-sayti
   ```

2. **Virtual Muhitni Yaratish:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Kerakli Kutubxonalarni O'rnatish:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Ma'lumotlar Bazasini Yaratish:**

   ```bash
   python manage.py migrate
   ```

5. **Loyihani Ishga Tushirish:**

   ```bash
   python manage.py runserver
   ```

6. **Brauzerda ochish:** `http://127.0.0.1:8000`

## Kelajakdagi Yaxshilanishlar

- Foydalanuvchilar uchun ro'yxatdan o'tish va login funksiyasi.
- Har bir yangilikka izoh qoldirish imkoniyati.
- Yangiliklarni qidirish funksiyasi.
- Ommabop yangiliklar bo'limi.


