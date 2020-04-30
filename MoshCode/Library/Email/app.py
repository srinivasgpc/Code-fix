from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib

#mime stands for multy



message = MIMEMultipart()

message["from"] = " KSK vivek"
message["to"] = "srinivagaddam423@gmail.com"
message["subject"] = "Auto genarate email with python"

message.attach(MIMEText("Email recieved from vivek"))
message.attach(MIMEImage(Path("vivek.jpg").read_bytes()))


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("touchinvivek@gmail.com", "v8008577345")
    smtp.send_message(message)
    print("sent..")

