from telegram.ext import Updater, CommandHandler
import logging

def setup_log():
    logging.basicConfig(level=logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def hello(bot, update):
    update.message.reply_text(
            'Hello {}'.format(update.message.from_user.first_name))


def start_polling(updater):
    updater.start_polling()
    updater.idle()


def start_webhook(updater, host='0.0.0.0', port=80, webhook_url=None):
    if webhook_url == None:
        raise ValueError('Webhook URL can not be None')

    updater.start_webhook(listen=host, port=port)
    updater.bot.set_webhook(webhook_url)
    updater.idle()


def run(token, execution_type='polling'):
    setup_log()

    updater = Updater(token)
    updater.dispatcher.add_handler(CommandHandler('hello', hello))

    if execution_type == 'webhook':
        start_webhook(updater)
    elif execution_type == 'polling':
        start_polling(updater)

