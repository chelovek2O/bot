import telebot
from telebot import types
token='7372198946:AAHod6XogSROYhrnv5pLyDCEMA02iGMxMQY'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет я бот для помощи коледжа IThub что бы начать нажмите /menu')

@bot.message_handler(commands=['menu'])

def button_message(message):
    
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("получить ссылку на наш сайт")
    item2=types.KeyboardButton("получить контакты приемной комиссии")
    item3=types.KeyboardButton("получить контакты куратора моей группы")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)

@bot.message_handler(content_types='text')

def message_reply(message):
    if message.text=="получить ссылку на наш сайт":
        bot.send_message(message.chat.id,"https://ithub.ru/") 

    if message.text=="получить контакты приемной комиссии":
        bot.send_message(message.chat.id,"88888888888  лялялля   и 999999999 лолололо")


    if message.text=="получить контакты куратора моей группы":

        bot.send_message(message.chat.id,"выберите номер вашей группы ")
        if message.text=="выберите номер вашей группы":
           item1=types.KeyboardButton("911")
           markup.add(item1)
bot.infinity_polling()
    


