# from shared.components.documents.generatePDFDocs import create_document
from shared.components.pymailer.mailer import send_email
from shared.database.mongo import takePlan, getWorkingPlan


def takeWorkingPlan(message, bot):
    bot.send_message(message.chat.id, "Чтобы взять план в работу, отправь мне цифру пункта меню")
    takePlan(message, bot)

    def first_step(message):
        try:
            plan_choosen = int(message.text)
            worker = f"{message.chat.first_name} {message.chat.last_name}"
            getWorkingPlan(plan_choosen, worker)
            bot.send_message(message.chat.id, "Данные обновлены!✅\nПлан взят в работу\nДля возврата в меню работы нажмите на команду: /work_start")
            # file_name = create_document(plan_choosen)
            # send_email(file_name)

        except Exception as e:
            bot.reply_to(message, 'oooops')
            print(e)

    bot.register_next_step_handler(message, first_step)


