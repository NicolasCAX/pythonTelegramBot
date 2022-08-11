from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os
import requests
import json

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}\nI am a sample Telegram bot made with PythonTelegramBot y el price de Bitcoin es de $!' + getBtc())

def getBtc():
    try:
      response = requests.get("https://www.bitstamp.net/api/v2/ticker/btcusd")
      response = response.json()
      return str("{:,.2f}".format(float(response["last"])))
    except:
      return getError()
   
    
updater = Updater(os.environ.get("TOKEN"), use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', start))

print("Bot started successfully")

updater.start_polling()
updater.idle()
