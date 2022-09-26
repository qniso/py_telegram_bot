from shared.database.mongo import takePlan, getWorkingPlan


def takeWorkingPlan(message, bot):
    bot.send_message(message.chat.id, "Чтобы взять план в работу, отправь мне цифру пункта меню")
    takePlan(message, bot)

    def first_step(message):
        try:
            plan_choosen = int(message.text)
            worker = f"{message.chat.first_name} {message.chat.last_name}"
            getWorkingPlan(plan_choosen, worker, bot, message)
            bot.send_message(message.chat.id, "Данные обновлены!✅\nПлан взят в работу\nДля возврата в меню работы нажмите на команду: /work_start")
        except Exception as e:
            bot.reply_to(message, 'oooops')
            print(e)

    #Добавить внесения имени исполнителя в вывод сообщений с планом
    bot.register_next_step_handler(message, first_step)


