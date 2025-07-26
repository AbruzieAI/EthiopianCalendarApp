# bot.py

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import datetime

TOKEN = "8355832823:AAFsX9r3I0LswUTj1NKEUR_GDxP0tI9pmrE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to the Ethiopian Calendar Bot!\n\nSend a Gregorian date (YYYY-MM-DD), and I’ll convert it to Ethiopian!")

def gregorian_to_ethiopian(g_date: datetime.date):
    # Rough conversion (better to use real conversion library)
    ethiopian_year = g_date.year - 8
    ethiopian_month = (g_date.month + 4) % 13 or 13
    ethiopian_day = g_date.day
    return f"{ethiopian_year}/{ethiopian_month:02d}/{ethiopian_day:02d}"

async def handle_date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    try:
        g_date = datetime.datetime.strptime(text, "%Y-%m-%d").date()
        et_date = gregorian_to_ethiopian(g_date)
        await update.message.reply_text(f"📅 Ethiopian Date: {et_date}")
    except ValueError:
        await update.message.reply_text("⚠️ Please send the date in YYYY-MM-DD format.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_date))

if __name__ == "__main__":
    app.run_polling()
