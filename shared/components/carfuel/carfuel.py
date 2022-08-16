import datetime

from shared.database.mongo import sendCarFuel, getCarsNumbers
from shared.classes.User_desc import Car_Fuel

def carFuel(message, bot):
    data = Car_Fuel()

    car_numbers = getCarsNumbers()
    print(car_numbers)

    bot.send_message(message.chat.id, "Напишите пожалуйста номер машины", reply_markup=None)

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
            bot.send_message(message.chat.id, f"Отлично, напишите сколько литров залито в машину под номером {carNum}", reply_markup=None)
            bot.register_next_step_handler(message, second_step)
        else:
            bot.send_message(message.chat.id, "Такой машины нет в базе, попробуйте ещё раз\nНапишите пожалуйста номер машины", reply_markup=None)
            bot.register_next_step_handler(message, first_step)

    bot.register_next_step_handler(message, first_step)

    def second_step(message):
        print('CHECK FUEL FUNC')
        fuel = message.text
        data.fuel = fuel
        print(fuel)
        print(fuel.isdigit())
        if not fuel.isdigit():
            print('Литры необходимо прописать только числом')
            bot.reply_to(message,
                         f'Литры необходимо прописать только числом\nНапишите пожалуйста, сколько литров залито в машину')
            bot.register_next_step_handler(message, second_step)
            return
        else:
            bot.send_message(message.chat.id, "DONE")
            sendCarFuel(data)







