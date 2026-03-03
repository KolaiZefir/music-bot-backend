import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from config import BOT_TOKEN

# Включаем максимальное логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)
logger = logging.getLogger(__name__)

async def handle_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обрабатываем ВСЕ обновления"""
    logger.debug("="*50)
    logger.debug("ПОЛУЧЕНО ОБНОВЛЕНИЕ:")
    logger.debug(f"Тип обновления: {type(update)}")
    
    # Проверяем разные типы сообщений
    if update.message:
        logger.debug(f"✅ Личное сообщение от @{update.message.from_user.username}")
        logger.debug(f"Текст: {update.message.text}")
    
    if update.channel_post:
        logger.debug(f"🔥🔥🔥 НАЙДЕНО СООБЩЕНИЕ ИЗ КАНАЛА! 🔥🔥🔥")
        logger.debug(f"ID канала: {update.channel_post.chat_id}")
        logger.debug(f"Текст: {update.channel_post.text}")
        
        if update.channel_post.audio:
            logger.debug(f"🎵 Найдено аудио!")
            
        if update.channel_post.video:
            logger.debug(f"🎬 Найдено видео!")
    
    if update.edited_message:
        logger.debug(f"✏️ Отредактированное сообщение")
    
    if update.message and update.message.forward_from_chat:
        chat = update.message.forward_from_chat
        logger.debug(f"📢 ПЕРЕСЛАНО ИЗ КАНАЛА:")
        logger.debug(f"Название: {chat.title}")
        logger.debug(f"ID канала: {chat.id}")
    
    logger.debug("="*50)

async def check_channel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Проверка пересланных сообщений из канала"""
    if update.message and update.message.forward_from_chat:
        chat = update.message.forward_from_chat
        print("\n" + "🔥"*50)
        print("НАЙДЕН КАНАЛ!")
        print(f"Название: {chat.title}")
        print(f"ID: {chat.id}")
        print(f"Тип: {chat.type}")
        print("🔥"*50 + "\n")
        
        await update.message.reply_text(
            f"✅ Канал найден!\n"
            f"Название: {chat.title}\n"
            f"ID: {chat.id}\n"
            f"Теперь отправьте музыку прямо в канал"
        )

def main():
    print("="*60)
    print("🔍 ТЕСТ КАНАЛА - ИСПРАВЛЕННАЯ ВЕРСИЯ")
    print("="*60)
    
    # Создаем приложение
    app = Application.builder().token(BOT_TOKEN).build()
    
    # Добавляем обработчики
    app.add_handler(MessageHandler(filters.ALL, handle_all))
    app.add_handler(MessageHandler(filters.FORWARDED, check_channel))
    
    print("✅ Бот запущен")
    print("\n📢 СДЕЛАЙТЕ ТРИ ДЕЙСТВИЯ:")
    print("   1. Напишите боту /start (проверка связи)")
    print("   2. Перешлите ЛЮБОЕ сообщение из канала боту")
    print("   3. Отправьте аудиофайл прямо в канал")
    print("\n👆 СМОТРИТЕ ЛОГИ ВЫШЕ")
    print("="*60)
    
    # Запускаем с ВСЕМИ типами обновлений
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()