import datetime
import pymongo
from shared.classes.User_desc import User_desc
import certifi
ca = certifi.where()

myclient = pymongo.MongoClient(
    "mongodb+srv://Admin_qniso:BUOorKChVrdWTWVu@telegrambot.n1ebp.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca
)

user = User_desc()

def connectMongo(data):
    db = myclient['TELEGRAM_BOT']  # TELEGRAM_BOT
    collection = db['PYTHON_TEST']  # PYTHON_TEST

    post = data.__dict__
    send_data = collection.insert_one(post)

def registerUser(data, bot, message):
    db = myclient['TELEGRAM_BOT']  # TELEGRAM_BOT
    collection = db['TG_REGISTERED_USERS']  # PYTHON_TEST

    cur = collection.find()
    res = list(cur)
    chat_id = None
    if(len(res) > 1 ):
        post = data.__dict__
        send_data = collection.insert_one(post)
        bot.send_message(message.chat.id, "Регистрация успешна ✅")
    else:
        x = list(collection.find({"chat_id": data.chat_id}))
        for i in x:
            chat_id = i["chat_id"]
        if(chat_id == data.chat_id):
            bot.send_message(message.chat.id, 'Вы уже зарегистрированны')
        else:
            post = data.__dict__
            send_data = collection.insert_one(post)
            bot.send_message(message.chat.id, "Регистрация успешна ✅")

def getCarsNumbers():
    db = myclient['TELEGRAM_BOT']  # TELEGRAM_BOT
    collection = db['CAR_NUMBERS']  # PYTHON_TEST

    data = collection.find_one()
    car_numbers = data["data"]
    return car_numbers

def sendCarFuel(data):
    db = myclient['TELEGRAM_BOT']  # TELEGRAM_BOT
    collection = db['TG_CAR_FUEL']  # PYTHON_TEST

    post = data.__dict__
    send_data = collection.insert_one(post)

def sendWorkingPlan(data, message, bot):
    db = myclient['TELEGRAM_BOT']  # TELEGRAM_BOT
    collection = db['WORKING_PLAN']  # PYTHON_TEST

    doc = collection.find().limit(1).sort("id", -1)  #

    cur = collection.find()
    res = list(cur)
    if (len(res) == 0):
        post = data.__dict__
        send_data = collection.insert_one(post)
        bot.send_message(message.chat.id, "План зарегистрирован успешно ✅\n"
                                            "Для возврата в меню работы нажмите на команду: /work_start")
    else:
        for x in doc:
            a = x
        data.id += a["id"]
        post = data.__dict__
        send_data = collection.insert_one(post)
        bot.send_message(message.chat.id, "План зарегистрирован успешно ✅\n"
                                            "Для возврата в меню работы нажмите на команду: /work_start")


def takePlan(message, bot):
    id = 0
    db = myclient['TELEGRAM_BOT']  # TELEGRAM_BOT
    collection = db['WORKING_PLAN']  # PYTHON_TEST

    doc = collection.find()
    result = []
    worker = []
    worker_name ="-"

    for x in doc:
        id+=1
        if (not len(x['worker']) == 0):
            for i in x['worker']:
                worker.append(i)
                worker_name = ', '.join(worker)
        else:
            worker_name = "-"

        full_result = '\n'.join(map(str, [f"\n{id}. Номер плана: {x['planNumber']}\n"
                                          f"Организатор: {x['userName']}\n"
                                          f"Исполнитель: {worker_name}\n"
                                          f"Описание:\n"
                                          f"{x['planText']}\n"]))
        result.append(full_result)
    bot.send_message(message.chat.id, "".join(result))
    return result

def getWorkingPlan(plan_num, worker, bot, message):
    db = myclient['TELEGRAM_BOT']  # TELEGRAM_BOT
    collection = db['WORKING_PLAN']  # PYTHON_TEST
    update_date = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    for x in collection.find({"id": plan_num}):
        worker_name = worker

        for i in collection.find({"id": plan_num}):
            result_status = collection.update_one({"id": plan_num}, {"$set": {"status": "В работе"}} )
            result_worker = collection.update_one({"id": plan_num}, {"$push": {"worker": worker}})
            result_update_time = collection.update_one({"id": plan_num}, {"$push": {"update_time": update_date}})




