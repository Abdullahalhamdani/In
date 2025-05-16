
# Telegram Online Monitor Bot

مراقبة حالة الاتصال لمستخدم تليغرام وإرسال تقارير تلقائيًا إلى الرسائل المحفوظة باستخدام Telethon.

---

## المتطلبات

- Python 3.7+
- مكتبة [Telethon](https://github.com/LonamiWebs/Telethon)
- حساب على [Render.com](https://render.com/) أو أي منصة دعم تشغيل دائم

---

## الملفات

- `main.py` – سكربت المراقبة الأساسي.
- `requirements.txt` – يحتوي على المكتبات المطلوبة:
  ```
  telethon
  ```

---

## طريقة الاستخدام (على Render)

1. أنشئ مستودع GitHub وارفع فيه الملفات التالية:
   - `main.py`
   - `requirements.txt`

2. اذهب إلى [Render.com](https://render.com/) وسجّل الدخول.

3. اختر **New > Background Worker**.

4. اربط المستودع الذي أنشأته.

5. في الإعدادات:

   - **Build Command**:
     ```bash
     pip install -r requirements.txt
     ```

   - **Start Command**:
     ```bash
     python main.py
     ```

   - **Environment Variables**:
     | Key        | Value              |
     |------------|--------------------|
     | `API_ID`   | (رقم API ID الخاص بك) |
     | `API_HASH` | (API Hash الخاص بك)  |
     | `USER_ID`  | (رقم ID للمستخدم المُراقب) |

> **ملاحظة:** لا ترفع ملفات الجلسة (`session.session`) إلى GitHub. أضفها إلى `.gitignore`.

---

## التنبيهات

- السكربت يرسل إشعار بدء المراقبة، ويسجل وقت الدخول والخروج بدقة.
- يتم إرسال النتائج إلى **الرسائل المحفوظة** الخاصة بك تلقائيًا.

---

## الدعم أو التعديلات
لأي تعديل على السكربت أو دعم إضافي، لا تتردد في التواصل.
