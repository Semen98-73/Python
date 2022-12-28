from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from credits import bot_token

bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
   context.bot.send_message(update.effective_chat.id, "Привет!")

def message(update, context):
   if update.message.text == "Привет":
       context.bot.send_message(update.effective_chat.id, "Привет! Как тебя зовут ?")
 
 

def get_day(update, context):
   keyboard = [
      [InlineKeyboardButton("Понедельник", callback_data='1')], [InlineKeyboardButton("Вторник", callback_data='2')],
      [InlineKeyboardButton("Среда", callback_data='3')],[InlineKeyboardButton("Четверг", callback_data='4')]
   ]
   update.message.reply_text("Выбери день недели: ", reply_markup = InlineKeyboardMarkup(keyboard))


start_handler = CommandHandler('start', start)
getday_handler = CommandHandler('getday', get_day)
message_handler = MessageHandler(Filters.text, message)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(getday_handler)
dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()