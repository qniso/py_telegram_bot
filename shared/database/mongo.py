
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
    print(res)
    if (len(res) == 0):
        post = data.__dict__
        send_data = collection.insert_one(post)
        bot.send_message(message.chat.id, "План зарегистрирован успешно ✅\n"
                                            "Для возврата в меню работы нажмите на команду: /work_start")
        print(data.__dict__)
    else:
        for x in doc:
            a = x
        data.id += a["id"]
        post = data.__dict__
        send_data = collection.insert_one(post)
        bot.send_message(message.chat.id, "План зарегистрирован успешно ✅\n"
                                            "Для возврата в меню работы нажмите на команду: /work_start")

        print(data.__dict__)

def takePlan(message, bot):
    id = 0
    db = myclient['TELEGRAM_BOT']  # TELEGRAM_BOT
    collection = db['WORKING_PLAN']  # PYTHON_TEST

    doc = collection.find()

    print()
    space = "\n"
    result = []

    for x in doc:
        id+=1
        result.append(x)
        # print(f"{id}. Номер плана: {x['planNumber']}\n"
        #       f"Организатор: {x['userName']}\n"
        #       f"Исполнитель: -\n"
        #       f"Описание:\n"
        #       f"{x['planText']}")

        bot.send_message(message.chat.id, f"{id}. Номер плана: {x['planNumber']}\n"
                                          f"Организатор: {x['userName']}\n"
                                          f"Исполнитель: -\n"
                                          f"Описание:\n"
                                          f"{x['planText']}")

    print(result)