import logging

from telegram.ext import Updater, CommandHandler, Filters
from .handlers import start, config_calendar

def setup_log():
    logging.basicConfig(level=logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def start_polling(updater):
    updater.start_polling()
    updater.idle()


def start_webhook(updater, host='0.0.0.0', port=80, webhook_url=None):
    if webhook_url == None:
        raise ValueError('Webhook URL can not be None')

    updater.start_webhook(listen=host, port=port)
    updater.bot.set_webhook(webhook_url)
    updater.idle()


def run(user_id, token, host, port, webhook_url, execution_type='polling',):
    setup_log()

    updater = Updater(token)
    updater.dispatcher.add_handler(CommandHandler('start', start,
                                   Filters.user(user_id=user_id)))
    updater.dispatcher.add_handler(CommandHandler('calendar', config_calendar,
                                   Filters.user(user_id=user_id)))

    if execution_type == 'webhook':
        start_webhook(updater, host, port, webhook_url)
    elif execution_type == 'polling':
        start_polling(updater)

