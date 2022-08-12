from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os
    
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}\nPrueba con PythonTelegramBot!')

    
updater = Updater(os.environ.get("TOKEN"), use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', start))

print("Bot started successfully")

updater.start_polling()
updater.idle()
