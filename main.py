from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from flask import Flask
import threading
import os

TOKEN = "8746516306:AAEse0EuPp7_8pI_dQ1e6lWjWsxdbj-yTjg"
app_web = Flask(__name__)

@app_web.route('/')
def home():
    return "Bot actif"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app_web.run(host="0.0.0.0", port=port)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Galaxy Rename Bot active 🚀")

bot = ApplicationBuilder().token(TOKEN).build()
bot.add_handler(CommandHandler("start", start))

threading.Thread(target=run_web).start()

bot.run_polling()
