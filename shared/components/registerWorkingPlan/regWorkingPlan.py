import datetime

from shared.classes.User_desc import WorkingPlan
from shared.database.mongo import sendWorkingPlan

def registerWorkingPlan(message, bot):
    id = 1
    data = WorkingPlan()

    data.id = id
    data.chat_id = message.chat.id
    data.userName = f"{message.chat.first_name} {message.chat.last_name}"
    data.userNickName = message.chat.username
    data.worker = []
    data.status = 'New'
    data.date = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    bot.send_message(message.chat.id, "Напишите пожалуйста номер нового плана")

    def first_step(message):
        data.planNumber = message.text
        data.planNumber.isdigit()
        bot.send_message(message.chat.id, f"Номер плана {data.planNumber}")
        bot.send_message(message.chat.id, "Напишите пожалуйста, что необходимо сделать")
        bot.register_next_step_handler(message, second_step)

    bot.register_next_step_handler(message, first_step)

    def second_step(message):
        data.planText = message.text
        bot.send_message(message.chat.id, f'План под номером: {data.planNumber}\n'
                                          f'Необходимо сделать:\n{data.planText}\n')
        sendWorkingPlan(data,message, bot)
        # print(data.__dict__)



