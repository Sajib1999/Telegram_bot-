import telebot
from telebot import types

TOKEN = "8097697242:AAE_Q0wWH_BNP2grnq88xF8tjmhfNNLNEXI"
bot = telebot.TeleBot(TOKEN)

# 🔐 আপনার Telegram ID (admin message এখানেই যাবে)
ADMIN_ID = @Mohammadsajib789  # এটা আপনার টেলিগ্রাম আইডি দিয়ে দিন

# 🔄 Dictionary: ইউজারের স্টেপ ট্র্যাক
user_step = {}

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
    user_id = message.chat.id

    # Step 1: Start Withdraw
    if message.text == "📤 উইথড্র রিকোয়েস্ট":
        bot.send_message(user_id, "💰 কত টাকা উইথড্র করবেন?")
        user_step[user_id] = "awaiting_amount"

    # Step 2: Get Amount
    elif user_step.get(user_id) == "awaiting_amount":
        user_step[user_id] = {"amount": message.text}
        bot.send_message(user_id, "📱 আপনার বিকাশ/নগদ নাম্বার দিন:")
        user_step[user_id]["step"] = "awaiting_number"

    # Step 3: Get Number & Confirm
    elif isinstance(user_step.get(user_id), dict) and user_step[user_id].get("step") == "awaiting_number":
        amount = user_step[user_id]["amount"]
        number = message.text

        # Send info to Admin
        bot.send_message(ADMIN_ID, f"📤 নতুন উইথড্র রিকোয়েস্ট:\n\n👤 ইউজার: @{message.from_user.username or 'No Username'}\n🆔 ID: {user_id}\n💰 পরিমাণ: {amount} টাকা\n📱 নাম্বার: {number}")

        bot.send_message(user_id, "✅ আপনার উইথড্র রিকোয়েস্ট পাঠানো হয়েছে। ধন্যবাদ।")
        user_step.pop(user_id)

    # Other Menu Buttons
    elif message.text == "🧑‍💼 আমার একাউন্ট":
        bot.send_message(user_id, f"🧾 আপনার টেলিগ্রাম ID: `{user_id}`", parse_mode="Markdown")
    elif message.text == "🎁 বোনাস চেক করুন":
        bot.send_message(user_id, "🎁 আপনি এখন পর্যন্ত 0 জনকে রেফার করেছেন। বোনাস: 0 টাকা")
    elif message.text == "📊 রেফার ইনকাম দেখুন":
        bot.send_message(user_id, "📊 এখন পর্যন্ত রেফার ইনকাম 0 টাকা")

bot.polling()
