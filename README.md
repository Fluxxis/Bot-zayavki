# Telegram Bot + Web-App

## 1) Бот

### Установка
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Настройка
Открой `bot.py` и вставь:
- `BOT_TOKEN`
- `WEBAPP_URL` (HTTPS, путь на твой `index.html`)

### Запуск
```bash
python bot.py
```

> По умолчанию используется polling. Если хочешь webhook — добавишь позже.

---

## 2) Web-App
Папка `webapp` (в отдельном архиве).

В `webapp/js/config.js` вставь свой Discord Webhook URL.
