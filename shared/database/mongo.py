import json
import pymongo
from shared.classes.User_desc import User_desc
import certifi
ca = certifi.where()

myclient = pymongo.MongoClient(
    "mongodb+srv://Admin_qniso:BUOorKChVrdWTWVu@telegrambot.n1ebp.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca
)

#ПРАВКИ -> Убрать копипаст функций, сократить колво кода

user = User_desc()

def connectMongo(data):
    db = myclient['TELEGRAM_BOT']  # TELEGRAM_BOT
    collection = db['PYTHON_TEST']  # PYTHON_TEST

    post = data.__dict__
    send_data = collection.insert_one(post)

def registerUser(data, bot, message):
    db = myclient['TELEGRAM_BOT']  # TELEGRAM_BOT
    collection = db['TG_REGISTERED_USERS']  # PYTHON_TEST

    for x in collection.find({"chat_id": data.chat_id}):
        if(not x == None):
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

