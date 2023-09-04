import telebot

bot = telebot.TeleBot('6472923985:AAH7wo3vHnW2ZW8txD21h2xNvxhH_oT2GFU')


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, 'ANYING')


@bot.message_handler(commands=['help'])
def welcome(message):
    bot.reply_to(message, 'BAPAK MU')


while True:
    try:
        bot.polling()
    except:
        pass
