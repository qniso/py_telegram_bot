from reportlab.pdfgen import canvas

def create_document():
    my_canvas = canvas.Canvas('/Users/roman.koriuk/py_telegram_bot/shared/components/documents/pdfDocs/first.pdf')
    my_canvas.drawString(100, 750, "Welcome to Reportlab!")
    my_canvas.save()