import telebot
import logging
import os

API_TOKEN = os.environ.get('API_TOKEN')

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)
bot = telebot.TeleBot(API_TOKEN)




bot.infinity_polling()