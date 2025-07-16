import telebot

TOKEN = "8097697242:AAE_Q0wWH_BNP2grnq88xF8tjmhfNNLNEXI"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "✅ বট এখন অনলাইনে!")

bot.polling()
