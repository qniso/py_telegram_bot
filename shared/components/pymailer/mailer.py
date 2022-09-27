import smtplib
from email.message import EmailMessage

def send_email():
    email_sender = 'mail.test.for.exmpl@gmail.com'
    email_pass = 'hbtvlzlkzgnelwcr'
    email_reciver = 'gnom51764@gmail.com'

    subject = 'TEST'
    body = "TEST"

    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_reciver
    em["Subject"] = subject
    em.set_content(body)

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(email_sender, email_pass)
        smtp.sendmail(email_sender, email_reciver, body)

