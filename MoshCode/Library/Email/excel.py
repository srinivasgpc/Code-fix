

import smtplib

from email.message import EmailMessage



msg = EmailMessage()
msg['Subject'] = 'Check out my excel!'
msg['From'] = 'vivek'
msg['To'] = "kasturi.vivek994@gmail.com"



msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is Vivek!</h1>
    </body>
</html>
""", subtype='html')


files = [ 'Book1.xlsx']

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename = file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login("touchinvivek@gmail.com", "v8008577345")
    smtp.send_message(msg)
    print('sent..')