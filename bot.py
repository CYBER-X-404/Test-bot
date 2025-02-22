from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler

TOKEN = "7445133123:AAGG1atZVQRMnUT97C0aHvafk0FunviFHBI"

def start(update, context):
    update.message.reply_text("Hello! I am running on Render.")

def main():
    bot = Bot(token=TOKEN)
    updater = Updater(bot=bot, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()