import os

from core.bot import run

TOKEN = os.environ.get('TELEGRAM_KEY')
HOST = os.environ.get('HOST')
PORT = int(os.environ.get('PORT'))
WEBHOOK_URL = os.environ.get('WEBHOOK_URL')
USER_ID = int(os.environ.get('USER_ID'))

if __name__ == '__main__':
    run(USER_ID, TOKEN, HOST, PORT, WEBHOOK_URL, 'webhook')


