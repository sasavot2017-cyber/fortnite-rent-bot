import os
import logging
from telegram import Update
from telegram.ext import (
    Application, CommandHandler, ContextTypes
)

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎮 Fortnite Rent Bot\n\n"
        "Добро пожаловать!\n"
        "Доступные команды:\n"
        "/rent — аренда\n"
        "/help — помощь"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "По вопросам аренды обращайтесь к администратору."
    )

async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ Нет доступа")
        return

    await update.message.reply_text(
        "⚙️ Панель администратора\n"
        "Бот работает!"
    )

def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN не задан")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("admin", admin))
    app.run_polling()

if __name__ == "__main__":
    main()
