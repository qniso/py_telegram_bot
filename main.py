import datetime
import telebot

from shared.classes.User_desc import User_desc
from shared.database.mongo import connectMongo, sendCarFuel
from shared.components.carfuel.carfuel import carFuel


bot = telebot.TeleBot("5316275912:AAGzAejn-Pa-8usVJ7eUYujH4-EwvO9B9W8")

@bot.message_handler(commands=['start'])
def start_message(message):
    user = User_desc()
    user.chat_id = message.chat.id
    user.userName = f"{message.chat.first_name} {message.chat.last_name}"
    user.userNickName = message.chat.username
    user.date = datetime.datetime.now()
    # Connection to mongoDB
    connectMongo(user)

    bot.send_message(message.chat.id, "Bot is working on python")


@bot.message_handler(commands=['work_start'])
def work_start(message):
    bot.register_next_step_handler(message, choice_step)
    bot.send_message(message.chat.id, "Необходимо выбрать вид работы из меню:\n1. Залить бензин\n2. Задать план\n3. Приступить к выполнению плана\n\nОтправь мне цифру пункта меню для того чтобы начать работу")


def choice_step(message):
    try:
        if(message.text == "1"):
            bot.reply_to(message, 'Вы выбрали залить бензин')
            carFuel(message, bot)
        elif(message.text == "2"):
            bot.reply_to(message, 'Вы выбрали задать план')
        elif (message.text == "3"):
            bot.reply_to(message, 'Вы выбрали приступить к выполнению плана')
        else:
            bot.send_message(message.chat.id, "Некорректный символ для выбора, попробуйте ещё раз")
            work_start(message)
    except Exception as e:
        bot.reply_to(message, 'oooops')



bot.polling(none_stop=True, interval=0)


