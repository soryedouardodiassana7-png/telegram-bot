from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

8746516306:AAHmQ9TYJE-hfJYRXdnXWRJ6zS1EXtVvb6s

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
await update.message.reply_text("Galaxy Rename Bot active 🚀")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
