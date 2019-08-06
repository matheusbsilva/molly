from telegram.ext import Updater, CommandHandler
import logging

def setup_log():
    logging.basicConfig(level=logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def hello(bot, update):
    update.message.reply_text(
            'Hello {}'.format(update.message.from_user.first_name))

def run(token):
    setup_log()

    updater = Updater(token)
    updater.dispatcher.add_handler(CommandHandler('hello', hello))
    updater.start_polling()
    updater.idle()
