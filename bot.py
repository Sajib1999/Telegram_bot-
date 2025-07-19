from telebot import TeleBot, types

bot = TeleBot("7481628411:AAFNNO0jxsND9lu9UK4m_9IPTNOVnJf_7mM")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(
        types.KeyboardButton("/promo"),
        types.KeyboardButton("/join")
    )
    markup.row(
        types.KeyboardButton("/offer"),
        types.KeyboardButton("/contact")
    )
    bot.send_message(message.chat.id, "👋 স্বাগতম! নিচের অপশন থেকে বেছে নিন:", reply_markup=markup)

@bot.message_handler(commands=['promo'])
def promo(message):
    bot.send_message(message.chat.id, "🎁 আজকের প্রমো কোড: OXY11")

@bot.message_handler(commands=['join'])
def join(message):
    bot.send_message(message.chat.id, "✅ সাব-এজেন্ট হতে এই ফর্ম পূরণ করুন:\nhttps://your-form-link.com")

@bot.message_handler(commands=['offer'])
def offer(message):
    bot.send_message(message.chat.id, "🔥 আজকের অফার: প্রথম ডিপোজিটে 100% বোনাস!")

@bot.message_handler(commands=['contact'])
def contact(message):
    bot.send_message(message.chat.id, "📞 যোগাযোগ করুন:\n📱 WhatsApp: +8801826444505\n💬 Telegram: @sajibvai")

bot.infinity_polling()
