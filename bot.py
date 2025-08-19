import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Получаем токен из переменной окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Простейшие обработчики команд
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Бот работает!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - запустить бота\n/help - список команд\n/geo - пример команды"
    )

# Здесь добавь остальные команды, например:
async def geo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Команда geo работает!")

# Главная функция
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Регистрируем команды
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("geo", geo))
    # Добавь здесь остальные команды по аналогии

    # Запуск бота
    app.run_polling()

if _name_==_"__main__":
    main()
