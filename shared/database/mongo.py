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

def registerUser(data):
    db = myclient['TELEGRAM_BOT']  # TELEGRAM_BOT
    collection = db['TG_REGISTERED_USERS']  # PYTHON_TEST

    post = data.__dict__
    send_data = collection.insert_one(post)

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

