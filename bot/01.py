import telebot
from telebot import types

token='7372198946:AAHod6XogSROYhrnv5pLyDCEMA02iGMxMQY'
bot=telebot.TeleBot(token)


# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id,'ghbdtn')
#     markup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton("Перейти в меню")
#     markup.row(btn1)

@bot.message_handler(commands=['start'])

def button_message(message):
    
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("ссылка на наш сайт",callback_game= '1')
    btn2 = types.InlineKeyboardButton("контакты приемной комиссии",callback_data= '2')
    btn3 = types.InlineKeyboardButton("контакты куратора моей группы",callback_data= '3')
    btn4 = types.InlineKeyboardButton("справка об обучении",callback_data= '4')
    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3)
    markup.row(btn4)
    
    bot.send_message(
        message.chat.id, "🧾 Выберите что бы вы хотели получить: ", reply_markup=markup
        
    )


@bot.message_handler(content_types='text')

def message_reply(message):
    if  callback.data == "ссылка на наш сайт":
         bot.send_message(message.chat.id,"https://ithub.ru/") 

    elif message.text=="контакты приемной комиссии":
        bot.send_message(message.chat.id,"88888888888  лялялля   и 999999999 лолололо")


    elif message.text=="контакты куратора моей группы":

        bot.send_message(message.chat.id,"выберите номер вашей группы ")
        if message.text=="выберите номер вашей группы":
           item1=types.KeyboardButton("911")
           markup.add(item1)
bot.infinity_polling()
    


