import telebot

TOKEN = "8097697242:AAE_Q0wWH_BNP2grnq88xF8tjmhfNNLNEXI "
bot = telebot.TeleBot(TOKEN)

AFFILIATE_LINK = "https://refpa3267686.top/L?tag=d_905607m_1622c_2023&site=905607&ad=1622"
PROMO_CODE = "Oxy11"
CONTACT_INFO = "+8801826444505 (WhatsApp & Telegram)"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        f"""👋 স্বাগতম {message.from_user.first_name}!

🎯 আপনি এখন 1xBet অফিশিয়াল সাব এজেন্টের সাথে আছেন।

🔗 অ্যাকাউন্ট খুলতে নিচের বাটনে ক্লিক করুন:
👉 {AFFILIATE_LINK}

🎁 Promo Code: {PROMO_CODE}
💰 100% বোনাস প্রথম ডিপোজিটে!

📞 যোগাযোগ: {CONTACT_INFO}
""",
        reply_markup=main_menu()
    )

def main_menu():
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("🟢 1xBet এ অ্যাকাউন্ট খুলুন", url=AFFILIATE_LINK))
    markup.add(telebot.types.InlineKeyboardButton("🎁 Promo Code: Oxy11", callback_data="promo"))
    markup.add(telebot.types.InlineKeyboardButton("📞 যোগাযোগ করুন", callback_data="contact"))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == "promo":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, f"🎁 আপনার Promo Code: {PROMO_CODE}")
    elif call.data == "contact":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, f"📞 যোগাযোগ: {CONTACT_INFO}")

bot.infinity_polling()
