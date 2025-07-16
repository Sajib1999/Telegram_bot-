import telebot
from telebot import types

TOKEN = "8097697242:AAE_Q0wWH_BNP2grnq88xF8tjmhfNNLNEXI"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("🧑‍💼 আমার একাউন্ট")
    btn2 = types.KeyboardButton("🎁 বোনাস চেক করুন")
    btn3 = types.KeyboardButton("📤 উইথড্র রিকোয়েস্ট")
    btn4 = types.KeyboardButton("📊 রেফার ইনকাম দেখুন")
    markup.add(btn1, btn2, btn3, btn4)

    bot.send_message(message.chat.id,
                     f"👋 স্বাগতম {message.from_user.first_name}!\n\nনীচের Menu থেকে অপশন বেছে নিন 👇",
                     reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == "🧑‍💼 আমার একাউন্ট":
        bot.send_message(message.chat.id, f"🧾 আপনার টেলিগ্রাম ID: `{message.from_user.id}`", parse_mode="Markdown")
    elif message.text == "🎁 বোনাস চেক করুন":
        bot.send_message(message.chat.id, "🎁 আপনি এখন পর্যন্ত 0 জনকে রেফার করেছেন। বোনাস: 0 টাকা")
    elif message.text == "📤 উইথড্র রিকোয়েস্ট":
        bot.send_message(message.chat.id, "📥 অনুগ্রহ করে @sajibvai_bot এ উইথড্র মেসেজ পাঠান")
    elif message.text == "📊 রেফার ইনকাম দেখুন":
        bot.send_message(message.chat.id, "📊 এখন পর্যন্ত রেফার ইনকাম 0 টাকা")

bot.polling()
