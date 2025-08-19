import os
import requests
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Получаем токен и chat_id из переменных окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")  # Можно использовать для отправки уведомлений самому себе

# Слова для поиска
SEARCH_TERMS = [
    "геотекстиль",
    "бентонітов",
    "георешітка",
    "геомембрана",
    "геосітка",
    "Протирадіаційного укриття нове будівництво",
    "Будівництво захисної споруди"
]

# Функция для поиска последних публикаций в Prozorro
def search_prozorro(query):
    url = f"https://prozorro.gov.ua/uk/search/tender?text={query}&sort=publication_date,desc"
    try:
        r = requests.get(url)
        r.raise_for_status()
        data = r.text
        # Простая проверка: берем первые 500 символов результата для примера
        return f"Results for '{query}':\n{data[:500]}...\nLink: {url}"
    except Exception as e:
        return f"Error fetching '{query}': {e}"

# Обработчик команды /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привіт! Я бот для пошуку тендерів на Прозорро. Використовуй /search_all для останніх результатів.")

# Обработчик команды /search_all
def search_all(update: Update, context: CallbackContext):
    messages = []
    for term in SEARCH_TERMS:
        result = search_prozorro(term)
        messages.append(result)
    # Отправляем все результаты
    for msg in messages:
        update.message.reply_text(msg)

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("search_all", search_all))

    updater.start_polling()
    updater.idle()

if name == "__main__":
    main()

import os
TOKEN = os.environ.get("TELEGRAM_TOKEN")

import os
from telegram.ext import Updater, CommandHandler

# Берём токен из переменной окружения
TOKEN = os.environ.get("TELEGRAM_TOKEN")

# Команда /start
def start(update, context):
    update.message.reply_text("Привет 👋! Я твой Prozorro бот. Напиши /help, чтобы увидеть список команд.")

# Команда /help
def help_command(update, context):
    update.message.reply_text(
        "/geo - Поиск по слову 'геотекстиль'\n"
        "/bentonit - Поиск по слову 'бентонітов'\n"
        "/georeshetka - Поиск по слову 'георешітка'\n"
        "/geomembrana - Поиск по слову 'геомембрана'\n"
        "/geosetka - Поиск по слову 'геосітка'\n"
        "/shelter - Поиск по слову 'Протирадіаційного укриття нове будівництво'\n"
        "/zashchita - Поиск по слову 'Будівництво захисної споруди'\n"
    )

# Пока сделаем простые заглушки для команд
def geo(update, context):
    update.message.reply_text("🔎 Результаты поиска по слову 'геотекстиль' (пока тест).")

def bentonit(update, context):
    update.message.reply_text("🔎 Результаты поиска по слову 'бентонітов' (пока тест).")

def georeshetka(update, context):
    update.message.reply_text("🔎 Результаты поиска по слову 'георешітка' (пока тест).")

def geomembrana(update, context):
    update.message.reply_text("🔎 Результаты поиска по слову 'геомембрана' (пока тест).")

def geosetka(update, context):
    update.message.reply_text("🔎 Результаты поиска по слову 'геосітка' (пока тест).")

def shelter(update, context):
    update.message.reply_text("🏗️ Поиск по слову 'Протирадіаційного укриття нове будівництво' (тест).")

def zashchita(update, context):
    update.message.reply_text("🏗️ Поиск по слову 'Будівництво захисної споруди' (тест).")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Регистрируем команды
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("geo", geo))
    dp.add_handler(CommandHandler("bentonit", bentonit))
    dp.add_handler(CommandHandler("georeshetka", georeshetka))
    dp.add_handler(CommandHandler("geomembrana", geomembrana))
    dp.add_handler(CommandHandler("geosetka", geosetka))
    dp.add_handler(CommandHandler("shelter", shelter))
    dp.add_handler(CommandHandler("zashchita", zashchita))

    # Запуск
    updater.start_polling()
    updater.idle()

if name == "__main__":
    main()
