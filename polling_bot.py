from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
from config import BOT_TOKEN, LOCAL_IP, PORT

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    web_app_url = f"https://{LOCAL_IP}:{PORT}/player"
    keyboard = [[InlineKeyboardButton("🎵 Открыть плеер", web_app={"url": web_app_url})]]
    
    await update.message.reply_text(
        "🎵 Бот работает! Нажми кнопку для плеера",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

print("="*50)
print("Запуск polling бота...")
print(f"IP: {LOCAL_IP}")
print(f"URL плеера: https://{LOCAL_IP}:{PORT}/player")
print("="*50)

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("✅ Бот запущен в режиме polling")
print("📱 Идите в Telegram и отправьте /start")
print("="*50)

app.run_polling()