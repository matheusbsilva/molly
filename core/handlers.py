def start(bot, update):
    message_welcome = 'Eai %s, eu sou a Molly e eu to aqui pra arrumar essa zona que você chama de vida' % update.message.from_user.first_name
    update.message.reply_text(message_welcome)

def config_calendar(bot, update):
    message_config = 'Configure a integração com o Google Calendar pra eu poder te ajudar, envie o TOKEN de autenticação para a API'
    update.message.reply_text(message_config)
