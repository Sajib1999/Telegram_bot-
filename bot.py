import telebot
from telebot import types

TOKEN = "8097697242:AAE_Q0wWH_BNP2grnq88xF8tjmhfNNLNEXI"
bot = telebot.TeleBot(TOKEN)

ADMIN_ID = 123456789  # 🛑 নিজের টেলিগ্রাম ID বসান (https://t.me/userinfobot)

user_step = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("📥 ডিপোজিট / উইথড্র")
    btn2 = types.KeyboardButton("📱 বিকাশ / নগদ নাম্বার")
    markup.add(btn1, btn2)

    bot.send_message(message.chat.id,
                     f"👋 স্বাগতম {message.from_user.first_name}!\n\nআপনি কী করতে চান? মেনু থেকে বেছে নিন 👇",
                     reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    user_id = message.chat.id

    if message.text == "📥 ডিপোজিট / উইথড্র":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("1xBet")
        btn2 = types.KeyboardButton("Linebet")
        markup.add(btn1, btn2)
        bot.send_message(user_id, "🔰 আপনি কোন প্ল্যাটফর্মে লেনদেন করবেন?", reply_markup=markup)
        user_step[user_id] = {"step": "select_platform"}

    elif user_step.get(user_id, {}).get("step") == "select_platform" and message.text in ["1xBet", "Linebet"]:
        user_step[user_id]["platform"] = message.text
        user_step[user_id]["step"] = "enter_amount"
        bot.send_message(user_id, "💰 কত টাকা ডিপোজিট/উইথড্র করতে চান?")

    elif user_step.get(user_id, {}).get("step") == "enter_amount":
        platform = user_step[user_id]["platform"]
        amount = message.text
        username = message.from_user.username or "NoUsername"

        bot.send_message(ADMIN_ID,
                         f"📥 নতুন {platform} ডিপোজিট/উইথড্র রিকোয়েস্ট:\n\n👤 ইউজার: @{username}\n🆔 ID: {user_id}\n💰 পরিমাণ: {amount} টাকা")

        bot.send_message(user_id, "✅ আপনার অনুরোধ গ্রহণ করা হয়েছে। আমরা খুব শীঘ্রই যোগাযোগ করব।")
        user_step.pop(user_id)

    elif message.text == "📱 বিকাশ / নগদ নাম্বার":
        bot.send_message(user_id, "📲 আমাদের পেমেন্ট নাম্বার:\n\n📌 বিকাশ: 018xxxxxxxx\n📌 নগদ: 017xxxxxxxx\n\nTk পাঠানোর পর আমাদের সাথে যোগাযোগ করুন।")

    else:
        bot.send_message(user_id, "❗ অনুগ্রহ করে মেনু থেকে একটি অপশন বেছে নিন।")

bot.polling()
