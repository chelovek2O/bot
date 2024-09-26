import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

token='токен'
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
    btn1 = types.InlineKeyboardButton("ссылка на наш сайт",callback_data= 'url_hub')
    btn2 = types.InlineKeyboardButton("контакты приемной комиссии",callback_data= 'PK')
    btn3 = types.InlineKeyboardButton("контакты куратора моей группы",callback_data= 'CUR')
    btn4 = types.InlineKeyboardButton("справка об обучении",callback_data= 'SPR')
    markup.add(btn1,btn2)
    markup.add(btn3,btn4)
    
    
    bot.send_message(
        message.chat.id,
        f""" 
<b>👋 Добро пожаловать, {message.from_user.first_name}!</b> 
              
📗 Для начала можешь ознакомиться с  возможностями бота : 
 /start      - <em>Запускает бота</em> 
 <em> если хотите получить ссылку на сайт нажмите кнопку: ссылка на наш сайт</em> 
 <em>если хотите получить актуальные контакты приемной комиссии нажмите кнопку: контакты приемной комиссии  </em> 
 <em>если хотите получить актуальные контакты  куратора вашей группы нажмите кнопку: контакты куратора моей группы</em> 
 
                     """,
        parse_mode="html",
        reply_markup=markup,
    )


@bot.callback_query_handler(func=lambda callback: True) 
def callback_message(callback): 
        markup = types.InlineKeyboardMarkup()

    
        if  callback.data == "url_hub":
         bot.send_message(callback.message.chat.id,"https://ithub.ru/") 

        elif callback.data=="PK":
         bot.send_message(callback.message.chat.id,"88888888888  лялялля   и 999999999 лолололо")


        elif callback.data=="CUR":
            markup = types.InlineKeyboardMarkup()
            cbtn1 = types.InlineKeyboardButton("информационые технологии",callback_data= 'ITcur')
            cbtn2 = types.InlineKeyboardButton("дизайн",callback_data= 'Dcur')
            cbtn3 = types.InlineKeyboardButton("маркетинг",callback_data= 'MKcur')
            cbtn4 = types.InlineKeyboardButton("разработка игр",callback_data= 'RIcur')
            markup.add(cbtn1,cbtn2)
            markup.add(cbtn3,cbtn4)
    
            bot.send_message(callback.message.chat.id,"выберите кафедру")

            if callback.data=="ITcur":
                 markup = types.InlineKeyboardMarkup()
                 ITcbtn1 = types.InlineKeyboardButton("первый курс",callback_data= '1cur')
                 ITcbtn2 = types.InlineKeyboardButton("второй курс",callback_data= '2cur')
                 ITcbtn3 = types.InlineKeyboardButton("третий курс",callback_data= '3cur')
                 ITcbtn4 = types.InlineKeyboardButton("четвертый курс ",callback_data= '4cur')
                 markup.add(ITcbtn1,ITcbtn2)
                 markup.add(ITcbtn3,ITcbtn4)
    
                 bot.send_message(callback.message.chat.id,"выберите курс")

            if callback.data=="1cur":
                 markup = types.InlineKeyboardMarkup()
                 ITcbtn1 = types.InlineKeyboardButton("9.24.1",callback_data= '9.24.1')
                 ITcbtn2 = types.InlineKeyboardButton("9.24.2",callback_data= '9.24.2')
                 ITcbtn3 = types.InlineKeyboardButton("9.24.3",callback_data= '9.24.3')
                 ITcbtn4 = types.InlineKeyboardButton("9.24.4 ",callback_data= '9.24.4')
                 markup.add(ITcbtn1,ITcbtn2)
                 markup.add(ITcbtn3,ITcbtn4)
    
                 bot.send_message(callback.message.chat.id,"выберите номер группы")
                 if callback.data=="2cur":
                  markup = types.InlineKeyboardMarkup()
                 IT2cbtn1 = types.InlineKeyboardButton("11.24.1",callback_data= '11.24.1')
                 IT2cbtn2 = types.InlineKeyboardButton("11.24.2",callback_data= '11.24.2')
                 IT2cbtn3 = types.InlineKeyboardButton("11.24.3",callback_data= '11.24.3')
                 IT2cbtn4 = types.InlineKeyboardButton("11.24.4 ",callback_data= '11.24.4')
                 markup.add(IT2cbtn1,IT2cbtn2)
                 markup.add(IT2cbtn3,IT2cbtn4)
    
                 bot.send_message(callback.message.chat.id,"выберите номер группы")

                 if callback.data=="3cur":
                  markup = types.InlineKeyboardMarkup()
                 IT3cbtn1 = types.InlineKeyboardButton("11.23.1",callback_data= '11.23.1')
                 IT3cbtn2 = types.InlineKeyboardButton("11.23.2",callback_data= '11.23.2')
                 IT3cbtn3 = types.InlineKeyboardButton("11.23.3",callback_data= '11.23.3')
                 IT3cbtn4 = types.InlineKeyboardButton("11.23.4 ",callback_data= '11.23.4')
                 markup.add(IT3cbtn1,IT3cbtn2)
                 markup.add(IT3cbtn3,IT3cbtn4)
    
                 bot.send_message(callback.message.chat.id,"выберите номер группы")
bot.infinity_polling()
    


