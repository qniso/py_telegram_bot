import requests
import datetime
import os

from shared.database.mongo import get_holiday_data
from shared.settings.settings import APIURL, TELEGRAM_API_URL


def generate_document_to_holiday(operation, data, message, bot):
    if(operation == "holiday"):
        date_start = data["date_start"]
        date_end = data["date_end"]
        full_name = data['userName']
        file_name = f'Заява на відпустку {full_name} {datetime.datetime.now().strftime("%m.%d.%Y")}.docx'


        send_file = requests.get(f'{APIURL}/document_gen',
                         params={'date_start': date_start, 'date_end': date_end, 'full_name': full_name})


        get_holiday_data(file_name)
        url = f'{TELEGRAM_API_URL}'
        method = url + 'sendDocument'

        with open(file_name, "rb") as file:
            files = {"document": file}
            title = f"Ваш документ на відпустку"
            chat_id = message.chat.id
            r = requests.post(method, data={"chat_id": chat_id, "caption": title}, files=files)
            bot.send_message(message.chat.id,
                             "Ваш документ на відпустку сформований, якщо зʼявляються питання щодо документу, то скористуйтеся командою /send_report, щоб оповістити адміна про помилку")
            if r.status_code != 200:
                raise Exception("send error")

        os.remove(file_name)
