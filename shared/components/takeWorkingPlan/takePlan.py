from shared.classes.User_desc import WorkingPlan
from shared.database.mongo import takePlan


def takeWorkingPlan(message, bot):
    bot.send_message(message.chat.id, "Vibirai plan")

    data = WorkingPlan()

    bot.send_message(message.chat.id, "Чтобы взять план в работу, отправь мне цифру пункта меню")

    # def first_step():
    takePlan(message,bot)
