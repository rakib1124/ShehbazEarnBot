from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = 8881368619:AAHgkjE53t53v7PZE4EULEJiPHdqFSzPhHU

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to Shehbaz Earn Bot!")

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
