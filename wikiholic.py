import wikipedia
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def get_article():
    title = wikipedia.random()
    page = wikipedia.page(title)

    return page

def make_message(page, sender_email, receiver_email):
    message = MIMEMultipart("alternative")
    message["Subject"] = "Wikiholic: " + page.title
    message["From"] = sender_email
    message["To"] = receiver_email

    plaintext = page.content
    fancytext = "<html>\n<body>\n" + page.html() + "\n<\body>\n<\html>"

    part1 = MIMEText(plaintext, "plain")
    part2 = MIMEText(fancytext, "html")

    message.attach(part1)
    message.attach(part2)

    return message

if __name__ == '__main__':
    page = get_article()

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "wikiholictoday@gmail.com"  # Enter your address
    receiver_email = "anastasija.tortevska@gmail.com"  # Enter receiver address
    password = input("Type your password and press enter: ")

    msg = make_message(page, sender_email, receiver_email)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg)

