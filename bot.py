import os
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# API & Bot Token (আপনার টেলিগ্রাম বট টোকেন বসান)
BOT_TOKEN = "7445133123:AAGG1atZVQRMnUT97C0aHvafk0FunviFHBI"
CHATGPT_API_URL = "https://chatgpt-by-paravi.tiiny.io?id=00&q="  # আপনার API

# Start Command
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! আমি তোমার AI bot 🤖\nএকটা মেসেজ পাঠাও, আমি উত্তর দেব।")

# ChatGPT Response Function
def chatgpt_reply(update: Update, context: CallbackContext):
    user_message = update.message.text
    api_url = CHATGPT_API_URL + requests.utils.quote(user_message)  # Query Encode

    try:
        response = requests.get(api_url)  # API Call
        if response.status_code == 200:
            reply_text = response.text.strip()
        else:
            reply_text = "আমি বুঝতে পারিনি 🧐"
    except Exception as e:
        reply_text = "কোনো সমস্যা হয়েছে, পরে চেষ্টা করুন 😞"

    update.message.reply_text(reply_text)

# Main Function
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Commands & Messages Handler
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, chatgpt_reply))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
