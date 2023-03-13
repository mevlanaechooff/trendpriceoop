import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail(toMail, subject, content):

    fromMail = "KIMDEN EMAIL"
    server = smtplib.SMTP("smtp.gmail.com",587)

    server.starttls()

    server.login(fromMail, "FROM MAİL SİFRE")

    message = MIMEMultipart('alternative')
    message['Subject']= subject

    htmlContent = MIMEText(content, 'html')
    message.attach(htmlContent)

    server.sendmail(
        fromMail,
        toMail,
        message.as_string()
    )
    print("Eposta gönderildi!")

    server.quit()