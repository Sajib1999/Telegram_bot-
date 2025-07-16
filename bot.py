import telebot
from telebot import types

API_TOKEN = '8097697242:AAE_Q0wWH_BNP2grnq88xF8tjmhfNNLNEXI'  # এখানে আপনার টোকেন বসান

bot = telebot.TeleBot(API_TOKEN)

user_payment_info = {}  # ইউজারের পেমেন্ট তথ্য রাখার dict

# ===== Main Menu =====
def send_main_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        types.KeyboardButton("📥 ডিপোজিট / উইথড্র"),
        types.KeyboardButton("🎁 বোনাস চেক করুন"),
        types.KeyboardButton("📱 বিকাশ / নগদ নাম্বার"),
        types.KeyboardButton("📞 যোগাযোগ করুন"),
        types.KeyboardButton("ℹ️ তথ্য / সাহায্য"),
        types.KeyboardButton("📰 স্পোর্টস নিউজ"),
        types.KeyboardButton("🎲 1xBet"),
        types.KeyboardButton("🎲 Linebet")
    )
    bot.send_message(chat_id, "স্বাগতম! নিচ থেকে অপশন বেছে নিন:", reply_markup=markup)

# ===== Deposit/Withdraw Menu =====
def deposit_withdraw_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        types.KeyboardButton("1xBet ডিপোজিট"),
        types.KeyboardButton("1xBet উইথড্র"),
        types.KeyboardButton("Linebet ডিপোজিট"),
        types.KeyboardButton("Linebet উইথড্র"),
        types.KeyboardButton("🔙 মেনুতে ফিরে যান")
    )
    return markup

# ===== Start Command Handler =====
@bot.message_handler(commands=['start'])
def start_handler(message):
    send_main_menu(message.chat.id)

# ===== Main Message Handler =====
@bot.message_handler(func=lambda message: True)
def message_handler(message):
    text = message.text
    chat_id = message.chat.id

    if text == "📥 ডিপোজিট / উইথড্র":
        bot.send_message(chat_id, "আপনার অপশন সিলেক্ট করুন:", reply_markup=deposit_withdraw_menu())

    elif text == "1xBet ডিপোজিট":
        ask_payment_info(message, platform="1xBet ডিপোজিট")

    elif text == "1xBet উইথড্র":
        bot.send_message(chat_id,
                         "1xBet উইথড্র সম্পর্কে বিস্তারিত জানার জন্য আমাদের সাথে যোগাযোগ করুন।\n"
                         "WhatsApp & Telegram: +8801826444505",
                         reply_markup=types.ReplyKeyboardRemove())

    elif text == "Linebet ডিপোজিট":
        ask_payment_info(message, platform="Linebet ডিপোজিট")

    elif text == "Linebet উইথড্র":
        bot.send_message(chat_id,
                         "Linebet উইথড্র সম্পর্কে বিস্তারিত জানতে যোগাযোগ করুন।\n"
                         "WhatsApp & Telegram: +8801826444505",
                         reply_markup=types.ReplyKeyboardRemove())

    elif text == "🎁 বোনাস চেক করুন":
        bot.send_message(chat_id,
                         "🎁 এক্সক্লুসিভ বোনাস অফার!\n\n"
                         "👉 1xBet প্রোমো কোড: Oxy11\n"
                         "👉 Linebet প্রোমো কোড: Oxy11\n\n"
                         "আরও বিস্তারিত জানতে যোগাযোগ করুন।",
                         reply_markup=types.ReplyKeyboardRemove())

    elif text == "📱 বিকাশ / নগদ নাম্বার":
        bot.send_message(chat_id,
                         "📲 পেমেন্ট নাম্বার:\n\n"
                         "📌 বিকাশ: 01912345678\n"
                         "📌 নগদ: 01898765432\n\n"
                         "টাকা পাঠানোর পর যোগাযোগ করুন।",
                         reply_markup=types.ReplyKeyboardRemove())

    elif text == "📞 যোগাযোগ করুন":
        bot.send_message(chat_id,
                         "📞 যোগাযোগ নম্বর:\n\n"
                         "WhatsApp & Telegram: +8801826444505\n"
                         "Email: example@example.com",
                         reply_markup=types.ReplyKeyboardRemove())

    elif text == "ℹ️ তথ্য / সাহায্য":
        bot.send_message(chat_id,
                         "এই বটের সাহায্যে আপনি সহজেই 1xBet ও Linebet এ ডিপোজিট এবং উইথড্র করতে পারবেন।\n"
                         "যেকোনো সমস্যা হলে যোগাযোগ করুন।",
                         reply_markup=types.ReplyKeyboardRemove())

    elif text == "📰 স্পোর্টস নিউজ":
        bot.send_message(chat_id,
                         "আজকের স্পোর্টস নিউজ:\n\n"
                         "🏆 আজকের প্রধান ম্যাচ: বাংলাদেশ বনাম ভারত\n"
                         "⚽ প্রিমিয়ার লিগ আপডেট: ম্যানচেস্টার ইউনাইটেড আজ ম্যাচ খেলবে\n"
                         "🏀 বাস্কেটবল ফাইনাল চলছে\n\n"
                         "আপডেট পেতে আমাদের সাথে থাকুন!",
                         reply_markup=types.ReplyKeyboardRemove())

    elif text == "🎲 1xBet":
        text_1xbet = (
            "🎯 1xBet রেফার লিঙ্ক:\n"
            "👉 https://1xbet6767.netlify.app/?tag=d_905607m_1622c_2023&site=905607&ad=1622\n\n"
            "💰 প্রোমো কোড: Oxy11\n"
            "রেজিস্ট্রেশন করতে এই লিঙ্ক ব্যবহার করুন এবং বোনাস নিন!"
        )
        bot.send_message(chat_id, text_1xbet, reply_markup=types.ReplyKeyboardRemove())

    elif text == "🎲 Linebet":
        text_linebet = (
            "🎯 Linebet রেফার লিঙ্ক:\n"
            "👉 https://linebet-login.netlify.app/?tag=d_905607m_1622c_2023&site=905607&ad=1622\n\n"
            "💰 প্রোমো কোড: Oxy11\n"
            "এই লিঙ্ক দিয়ে সাইন আপ করুন এবং বোনাস পান!"
        )
        bot.send_message(chat_id, text_linebet, reply_markup=types.ReplyKeyboardRemove())

    elif text == "🔙 মেনুতে ফিরে যান":
        send_main_menu(chat_id)

    else:
        bot.send_message(chat_id, "দয়া করে মেনু থেকে একটি অপশন সিলেক্ট করুন।")

# ===== Payment Info Collection =====
def ask_payment_info(message, platform):
    msg = (f"🎯 {platform} করার জন্য ধন্যবাদ!\n\n"
           "দয়া করে নিচের ফরম্যাটে আপনার পেমেন্ট তথ্য দিন:\n"
           "👉 আপনার নাম্বার এবং পাঠানো টাকা পরিমাণ স্পেস দিয়ে লিখুন\n"
           "উদাহরণ: 01912345678 500\n\n"
           "টাকা পাঠানোর পর অবশ্যই এই তথ্য দিতে হবে।")
    bot.send_message(message.chat.id, msg)
    bot.register_next_step_handler(message, save_payment_info)

def save_payment_info(message):
    text = message.text.strip()
    parts = text.split()
    if len(parts) == 2 and parts[1].isdigit():
        number = parts[0]
        amount = parts[1]
        user_payment_info[message.chat.id] = {'number': number, 'amount': amount}
        bot.send_message(message.chat.id,
                         f"আপনার পেমেন্ট তথ্য গ্রহণ করা হয়েছে:\n\nনম্বর: {number}\nটাকা: {amount} টাকা\n\nআপনার রিকোয়েস্ট প্রক্রিয়াকরণ হচ্ছে। ধন্যবাদ!")
        # চাইলে এখানে অ্যাডমিন নোটিফিকেশন কোড যুক্ত করতে পারেন
    else:
        bot.send_message(message.chat.id,
                         "⚠️ ভুল ফরম্যাট! দয়া করে আবার নাম্বার এবং টাকা পরিমাণ স্পেস দিয়ে লিখুন।\nউদাহরণ: 01912345678 500")
        bot.register_next_step_handler(message, save_payment_info)

# ===== Run Bot =====
bot.infinity_polling()
