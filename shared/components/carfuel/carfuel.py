import datetime

from shared.database.mongo import sendCarFuel, getCarsNumbers
from shared.classes.User_desc import Car_Fuel

def carFuel(message, bot):
    data = Car_Fuel()

    car_numbers = getCarsNumbers()

    bot.send_message(message.chat.id, "Напишите пожалуйста номер машины")

    def search(list, car_num):
        for i in range(len(list)):
            if list[i] == car_num:
                return True
        return False

    data.chat_id = message.chat.id
    data.userName = f"{message.chat.first_name} {message.chat.last_name}"
    data.userNickName = message.chat.username
    data.date = datetime.datetime.now()

    def first_step(message):
        carNum = message.text
        data.car_number = carNum
        if search(car_numbers, carNum):
            bot.send_message(message.chat.id, f"Отлично, напишите сколько литров залито в машину под номером {carNum}")
            bot.register_next_step_handler(message, second_step)
        else:
            bot.send_message(message.chat.id, "Такой машины нет в базе, попробуйте ещё раз\n"
                                              "Напишите пожалуйста номер машины")
            bot.register_next_step_handler(message, first_step)

    bot.register_next_step_handler(message, first_step)

    def second_step(message):
        fuel = message.text
        data.fuel = fuel
        if not fuel.isdigit():
            print('Литры необходимо прописать только числом')
            bot.reply_to(message,
                         f'Литры необходимо прописать только числом\n'
                         f'Напишите пожалуйста, сколько литров залито в машину')
            bot.register_next_step_handler(message, second_step)
            return
        else:
            bot.send_message(message.chat.id, "Данные отправлены!")
            sendCarFuel(data)







