from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = '8155759410:AAG-8zY2dgaPv6AVZBaAvwWK9v_5ePWLybQ'

# Функція для старту гри
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привіт! Цей бот дозволяє грати в гру про рибалку. Натисни 'Грати', щоб почати.")

# Запуск бота
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    print("Бот запущено!")
    app.run_polling()
