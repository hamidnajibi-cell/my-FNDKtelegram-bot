import telebot
from telebot import types

TOKEN = '8927165807:AAE442-HqiRTKXXEx4p6V3Qn0iSo2MTmKd0' # توکن خودت را اینجا بگذار
bot = telebot.TeleBot(TOKEN)

# سوالات و جواب‌ها
FAQ = {
    "1": {"q": "بهترین صرافی پیشنهادی برای اتصال به FNDK کدام صرافی است؟", "a": "همه عزیزان صرافی XT عضو بشین. 🚀\nصرافی ایکس تی یکی از معدود صرافی‌های بزرگ و معتبر ارز دیجیتال در جهان است که بدون محدودیت به کاربران ایرانی خدمات ارائه می‌دهد.\nلینک عضویت:\nhttps://www.xt.com/en/accounts/register?ref=VQTHEO"},
    
    "2": {"q": "چرا صرافی ایرانی پیشنهاد نمیکنید؟", "a": "به این دلیل که از FNDK به صرافی ها از آدرس کیف پولهای مشخص منتقل میشه و صرافی ها متصل هستند به هوش مصنوعی و آدرس رو تشخیص میدهند و بلاک میکنند. بهترین راه حل انتقال از FNDK به صرافی XT و سپس به صرافی داخلی است. 🛡️"},
    
    "3": {"q": "چرا وقتی به FNDK مراجعه می کنیم با صفحه سفید Phishing مواجه میشویم؟", "a": "سایت کلود فلر یک سری خدمات امنیتی به سایت‌ها میده تا از حملات دیداس و سایبری در امان باشند. این یک مورد امنیتی استاندارد است. 🛡️"},
    
    "4": {"q": "راهنمایی عضویت در صرافی XT رو از کجا میتونم پیدا کنم؟", "a": "بزودی آموزش تصویری براتون میزارم. عضویت ساده است و فقط حتما لینک زیر را بدون فیلترشکن باز کنید:\nhttps://www.xt.com/en/accounts/register?ref=VQTHEO"}
}

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    for key in FAQ:
        # اینجا متن دکمه، سوال است اما کد دکمه (callback_data) فقط شماره است
        btn = types.InlineKeyboardButton(FAQ[key]["q"], callback_data=key)
        markup.add(btn)
    
    bot.send_message(message.chat.id, "سلام! خوش آمدید. سوال خود را انتخاب کنید:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "back":
        # بازگشت به منو
        markup = types.InlineKeyboardMarkup(row_width=1)
        for key in FAQ:
            btn = types.InlineKeyboardButton(FAQ[key]["q"], callback_data=key)
            markup.add(btn)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                             text="لطفاً یکی از سوالات زیر را انتخاب کنید:", reply_markup=markup)
    
    elif call.data in FAQ:
        # نمایش پاسخ
        data = FAQ[call.data]
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🔙 بازگشت", callback_data="back"))
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                             text=f"❓ {data['q']}\n\n✅ {data['a']}", reply_markup=markup)

print("Bot is running...")
bot.infinity_polling()
