
import os
import logging
import threading
from flask import Flask
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

logging.basicConfig(level=logging.INFO)
TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

web = Flask(__name__)

@web.route("/")
def home():
    return "Fortnite Rent Bot is running!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎮 FORTNITE RENT BOT\n\n"
        "Добро пожаловать!\n\n"
        "/rent — аренда\n"
        "/help — помощь\n"
        "/id — узнать свой ID\n"
        "/admin — панель администратора"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "По вопросам аренды обращайтесь к администратору."
    )

async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Твой Telegram ID: {update.effective_user.id}"
    )

async def rent(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎮 Аренда Fortnite\n"
        "Система аренды скоро будет подключена."
    )

async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID or ADMIN_ID == 0:
        await update.message.reply_text("⛔ Нет доступа")
        return

    await update.message.reply_text(
        "⚙️ Панель администратора\n"
        "Бот работает!"
    )

def run_bot():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("id", get_id))
    application.add_handler(CommandHandler("rent", rent))
    application.add_handler(CommandHandler("admin", admin))
    application.run_polling()

if __name__ == "__main__":
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN is missing")

    threading.Thread(target=run_bot, daemon=True).start()
    web.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )

