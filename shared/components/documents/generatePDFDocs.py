from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, Frame, Spacer

import datetime

from shared.database.mongo import getWorkingPlanForDocument


def create_document(plan_choosen):

    data = getWorkingPlanForDocument(plan_choosen)
    date = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    format_data = ''.join(map(str,data))
    # print(data)



    # print(format_data)

    # FONT REGISTRATION
    pdfmetrics.registerFont(TTFont('Roboto', 'shared/components/documents/Fonts/Roboto-Regular.ttf'))

    file_name = f'{data[0]}.pdf'
    my_canvas = canvas.Canvas(f'shared/components/documents/pdfDocs/{file_name}')
    my_canvas.setFont('Roboto', 12)
    my_canvas.drawString(30, 750, f"TESTING PDF DOCUMENT")
    my_canvas.drawString(30, 735, f"DATA GIVES FROM MONGODB")
    my_canvas.drawString(480, 750, f"{date}")
    my_canvas.line(480, 747, 580, 747)
    my_canvas.drawString(30, 710, f"WORKING PLAN")
    print(data)
    print()
    a = 680
    for i in data:

        my_canvas.drawString(30, a, f"{i}")
        a = a - 15
        # print(i)
    # my_canvas.drawString(30, 710, f"{format_data}")
    my_canvas.save()

    return file_name