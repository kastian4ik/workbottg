import telebot
import os
import time
from flask import Flask
from threading import Thread

# ===== Telegram Bot =====
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# Словник для відомих учасників {chat_id: set(user_id)}
known_members = {}

# ===== Flask для UptimeRobot =====
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive!"

# ===== Хендлер всіх повідомлень для визначення chat_id супергрупи =====
@bot.message_handler(func=lambda m: True)
def catch_chat_id(message):
    chat_id = message.chat.id
    if chat_id not in known_members:
        known_members[chat_id] = set()
        print(f"[INFO] Новий chat_id визначено: {chat_id}")

# ===== Хендлер нових учасників =====
@bot.message_handler(content_types=['new_chat_members'])
def greet_new_member(message):
    chat_id = message.chat.id
    if chat_id not in known_members:
        known_members[chat_id] = set()

    for new_member in message.new_chat_members:
        if new_member.id not in known_members[chat_id]:
            mention = f"@{new_member.username}" if new_member.username else new_member.first_name
            text = (
                f"👋 Ласкаво просимо, {mention}!\n\n"
                f"Гілки для всього є, тож не загубишся 😎\n"
                f"Закидай фотку свого VAG, хай всі заздрять 🚗💨"
            )
            try:
                bot.send_message(chat_id, text)
                known_members[chat_id].add(new_member.id)
            except telebot.apihelper.ApiTelegramException as e:
                print(f"[WARNING] Помилка при надсиланні повідомлення: {e}")

print("✅ Бот запущений і працює 24/7...")

# ===== Стійкий polling з автоперезапуском =====
def run_bot():
    while True:
        try:
            bot.polling(none_stop=True, interval=1, timeout=20)
        except Exception as e:
            print(f"[ERROR] Помилка polling: {e}. Перезапуск через 5 секунд...")
            time.sleep(5)

# ===== Запуск Flask + Telegram Bot =====
if __name__ == "__main__":
    # Запускаємо бота в окремому потоці
    Thread(target=run_bot).start()
    # Запускаємо Flask для UptimeRobot
    app.run(host="0.0.0.0", port=8080)
