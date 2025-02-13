import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask, request
import os

TOKEN = "7999771914:AAGMXpgv_K_Pq2DUd5gZy9ibw5Anv2ABBVI"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# 🎯 Start buyrug'iga javob
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("ℹ Biz haqimizda", callback_data="about"),
        InlineKeyboardButton("📄 Hujjat topshirish", url="https://forms.gle/HcjAzsaKxMoimhvM6"),
        InlineKeyboardButton("🌍 Tilni o'zgartirish", callback_data="change_lang")
    )

    bot.send_message(message.chat.id, "👋 Assalomu alaykum! Kerakli bo‘limni tanlang:", reply_markup=markup)

# ℹ Biz haqimizda tugmachasiga javob
@bot.callback_query_handler(func=lambda call: call.data == "about")
def about_info(call):
    text = (
        "📌 *Biz haqimizda*\n\n"
        "🚀 *iMarketing Agency* – biznesingizni rivojlantirishga yordam beradigan zamonaviy marketing agentligi.\n"
        "Biz mijozlarimizga samarali marketing strategiyalari, brendni targ‘ib qilish, ijtimoiy tarmoqlarda rivojlantirish "
        "va raqamli reklama xizmatlarini taqdim etamiz.\n\n"
        "🎯 *Xizmatlarimiz:*\n"
        "🔹 SMM boshqaruv – Instagram, Facebook, TikTok va boshqa platformalarda professional yuritish\n"
        "🔹 Kontent marketing – kreativ postlar va reklama dizaynlari\n"
        "🔹 Targeting va reklama – auditoriyangizga mos reklamalar yaratish\n"
        "🔹 Brend strategiyasi – biznesingiz uchun eng yaxshi rivojlanish yo‘nalishi\n"
        "🔹 Zapusk va sotuvni oshirish – mahsulot va xizmatlarni bozorga chiqarish va sotuvni kuchaytirish\n\n"
        "💡 *Kimlar bilan ishlaymiz?*\n"
        "✅ Tadbirkor va biznes egalari\n"
        "✅ Mahsulot va xizmatlarini sotuvga chiqarayotgan startaplar\n"
        "✅ Xususiy ta’lim muassasalari (maktab, bog‘cha, o‘quv markazlari)\n"
        "✅ Shifokorlar, klinikalar va tibbiyot sohasi vakillari\n"
        "✅ Shaxsiy brendini rivojlantirishni xohlagan mutaxassislar\n\n"
        "⚡️ *Nega aynan biz?*\n"
        "✔️ 100+ muvaffaqiyatli loyiha\n"
        "✔️ O‘z sohasida tajribali mutaxassislar jamoasi\n"
        "✔️ Samarali va halol marketing strategiyalari\n"
        "✔️ Kreativ yondashuv va natijaga yo‘naltirilgan rejalashtirish\n\n"
        "📞 +998 97 577 21 25\n"
        "📩 @imarketinguzadmin"
    )
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown")

# 🌍 Tilni o'zgartirish tugmachasi
@bot.callback_query_handler(func=lambda call: call.data == "change_lang")
def change_language(call):
    lang_markup = InlineKeyboardMarkup()
    lang_markup.row_width = 2
    lang_markup.add(
        InlineKeyboardButton("🇺🇿 O'zbek", callback_data="lang_uz"),
        InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru")
    )
    bot.send_message(call.message.chat.id, "🌍 Tilni tanlang / Выберите язык:", reply_markup=lang_markup)

# 🌍 Til o'zgartirilganda
@bot.callback_query_handler(func=lambda call: call.data.startswith("lang_"))
def language_selected(call):
    lang = "O'zbek" if call.data == "lang_uz" else "Русский"
    bot.send_message(call.message.chat.id, f"✅ Til o'zgartirildi: {lang}")

# Webhook funksiyalari
@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "Bot ishlayapti!", 200

@app.route('/')
def webhook():
    bot.remove_webhook()
    full_url = "https://cb0ae4a1-58e9-4f8f-8e56-4e3d7ecd8587-00-123mod01af2ou.pike.replit.dev/" + TOKEN
    bot.set_webhook(url=full_url)
    return f"Webhook set to: {full_url}", 200

# Flask serverni ishga tushirish
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
