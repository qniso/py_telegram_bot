from shared.classes.User_desc import Holiday
from shared.components.documents.generatePDFDocs import generate_document_to_holiday
from shared.components.pymailer.mailer import send_email
from shared.database.mongo import send_holiday


def setHoliday(message, bot):

    bot.send_message(message.chat.id, "Напишите пожалуйста дату начала отпуска\nК примеру 01.01.2022")
    holiday = Holiday()

    holiday.chat_id = message.chat.id
    holiday.userName = f"{message.chat.first_name} {message.chat.last_name}"
    holiday.userNickName = message.chat.username
    holiday.date_start = ''
    holiday.date_end = ''
    # data.date = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    def first_step(message):
        holiday.date_start = message.text
        worker = f"{message.chat.first_name} {message.chat.last_name}"
        bot.send_message(message.chat.id, "Напишите пожалуйста дату конца отпуска")
        bot.register_next_step_handler(message, second_step)

    bot.register_next_step_handler(message, first_step)

    def second_step(message):
        holiday.date_end = message.text

        bot.send_message(message.chat.id, f"Ваш отпуск с {holiday.date_start} по {holiday.date_end} обратывается")
        print(holiday.__dict__)
        send_holiday(holiday, message, bot)
        generate_document_to_holiday('holiday', holiday.__dict__, message, bot)


    # first_step(message, bot)