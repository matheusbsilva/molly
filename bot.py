from telegram.ext import Updater, CommandHandler
import os

TOKEN = os.environ.get('TELEGRAM_KEY')

def hello(bot, update):
    print('--- Hello command ---')
    update.message.reply_text(
            'Hello {}'.format(update.message.from_user.first_name))

def run(token):
    print('--- Running bot ---')
    updater = Updater(token)
    updater.dispatcher.add_handler(CommandHandler('hello', hello))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    run(TOKEN)
