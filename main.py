import base64
import datetime
import telebot

from shared.classes.User_desc import User_desc
from shared.components.holidays.setHoliday import setHoliday
from shared.components.registerWorkingPlan.regWorkingPlan import registerWorkingPlan
from shared.components.takeWorkingPlan.takePlan import takeWorkingPlan
from shared.database.mongo import connectMongo, registerUser
from shared.components.carfuel.carfuel import carFuel
from shared.settings.settings import BOT_TOKEN

bot = telebot.TeleBot(f"{BOT_TOKEN}")

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

@bot.message_handler(commands=['register'])
def registration(message):
    user = User_desc()
    #
    user.chat_id = message.chat.id
    user.userFirstName = f"{message.chat.first_name}"
    user.userLastName = f"{message.chat.last_name}"
    user.userNickName = message.chat.username
    user.date = datetime.datetime.now()
    # try:
    registerUser(user, bot, message)
    # except Exception as e:
    #     print(e)
    #     bot.reply_to(message, 'oooops')

    # except Exception as e:
    #     print(e)
    #     bot.reply_to(message, 'oooops')

@bot.message_handler(commands=['holiday'])
def holiday(message):
        user = User_desc()

        user.chat_id = message.chat.id
        user.userFirstName = f"{message.chat.first_name}"
        user.userLastName = f"{message.chat.last_name}"
        user.userNickName = message.chat.username
        user.date = datetime.datetime.now()

        setHoliday(message, bot)

def choice_step(message):
    try:
        if(message.text == "1"):
            bot.reply_to(message, 'Вы выбрали залить бензин')
            carFuel(message, bot)
        elif(message.text == "2"):
            bot.reply_to(message, 'Вы выбрали задать план')
            registerWorkingPlan(message, bot)
        elif (message.text == "3"):
            bot.reply_to(message, 'Вы выбрали приступить к выполнению плана')
            takeWorkingPlan(message, bot)
        else:
            bot.send_message(message.chat.id, "Некорректный символ для выбора, попробуйте ещё раз")
            work_start(message)
    except Exception as e:
        bot.reply_to(message, 'oooops')
        print(e)



bot.polling(none_stop=True, interval=0)


