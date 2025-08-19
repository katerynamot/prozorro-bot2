Жена ❤️, [19.08.2025 12:16]
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

Жена ❤️, [19.08.2025 12:54]
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Вставь сюда токен твоего бота
TOKEN = '8415556073:AAHQrdf7mZ8XLU3jxWKBqKiTZs1iyKKJKIU'

# Обработчики команд
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот для поиска тендеров Prozorro.")

async def geotextil(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ищем тендеры по геотекстилю...")

async def bentonit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ищем тендеры по бентониту...")

async def georeshetka(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ищем тендеры по георешетке...")

async def geomembrana(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ищем тендеры по геомембране...")

async def geosetka(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ищем тендеры по геосетке...")

async def ukryttya(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ищем протирадиационные укрытия...")

async def zakhysna_sporuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ищем строительство защитных сооружений...")

# Создаем приложение бота
app = ApplicationBuilder().token(TOKEN).build()

# Регистрируем команды
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("geotextil", geotextil))
app.add_handler(CommandHandler("bentonit", bentonit))
app.add_handler(CommandHandler("georeshetka", georeshetka))
app.add_handler(CommandHandler("geomembrana", geomembrana))
app.add_handler(CommandHandler("geosetka", geosetka))
app.add_handler(CommandHandler("ukryttya", ukryttya))
app.add_handler(CommandHandler("zakhysna_sporuda", zakhysna_sporuda))

# Запуск бота
app.run_polling()
