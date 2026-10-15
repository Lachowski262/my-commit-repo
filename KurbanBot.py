import telebot 

TOKEN = "8814187918:AAHkb51kqYlPTev3NHLi3rgBjb5MCnevsX0"
ADMIN_CHAT_ID = ""    

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    global ADMIN_CHAT_ID

    print(message.chat.id)  

    if not ADMIN_CHAT_ID:
        ADMIN_CHAT_ID = str(message.chat.id)
        print("ADMIN_CHAT_ID установлен:", ADMIN_CHAT_ID)

    bot.send_message(
        ADMIN_CHAT_ID,
        f"Сенің Chat ID: {message.chat.id}"
    )

bot.polling()
