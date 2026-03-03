from config import BOT_TOKEN, LOCAL_IP, PORT

print(f"Токен: {BOT_TOKEN}")
print(f"Длина токена: {len(BOT_TOKEN)}")
print(f"IP: {LOCAL_IP}")
print(f"Порт: {PORT}")

if BOT_TOKEN and len(BOT_TOKEN) > 40:
    print("✅ Все хорошо, можно запускать бота!")
else:
    print("❌ Что-то не так с токеном")