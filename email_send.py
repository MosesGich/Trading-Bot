from email.message import EmailMessage
import ssl
import smtplib


def email_send(m, t, direction):
    e_sender = "gichohim27@gmail.com"
    e_pass = "tuvdtgxwesgclheg"
    e_receiver = "mosemuthoni57@gmail.com"

    subject = "Trade"
    body = "{} {} on TF{}".format(direction, m, t)

    em = EmailMessage()
    em['From'] = e_sender
    em['To'] = e_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(e_sender, e_pass)
        smtp.sendmail(e_sender, e_receiver, em.as_string())