# Логируем ошибки
import logging

# Логируем токен телеграм
import settings

# Подключаемся
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

# Файл для логирования
logging.basicConfig(format='%(asctime)s - %(levelname)s  - %(message)s',
					level=logging.INFO,
					filename='bot.log'
					)

def start_bot(update: Updater, context: CallbackContext):
	mytext = """Приветствуем тебя {}

	Это частный чат-бот CrowdWiz для Евгения и Виталия""".format(update.message.chat.first_name)
	logging.info('User {} press button /start'.format(update.message.chat.username))
	
	update.message.reply_text(mytext)

def chat(update: Updater, context: CallbackContext):
	text = update.message.text
	logging.info(text)

	update.message.reply_text(text)

def main():
	updtr = Updater('1766791115:AAG9KiAlVOR67iDx3Qyq4pV8TfOJO9KLLNw')

	#'1766791115:AAG9KiAlVOR67iDx3Qyq4pV8TfOJO9KLLNw'
	#settings.TOKEN_TELEGRAMM

	updtr.dispatcher.add_handler(CommandHandler("start", start_bot))
	updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))

	updtr.start_polling()
	updtr.idle()

if __name__ == "__main__":
	logging.info('Bot started!')
	main()