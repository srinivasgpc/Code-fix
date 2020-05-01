

import smtplib
import schedule
import time
from email.message import EmailMessage



msg = EmailMessage()
msg['Subject'] = 'Check out my excel!'
msg['From'] = 'vivek'
msg['To'] = "kasturi.vivek994@gmail.com"


def time1():
    msg.add_alternative("""\
    <!DOCTYPE html>
    <html>
        <body>
            <h1 style="color:SlateGray;">This is Vivek!</h1>
        </body>
    </html>
    """, subtype='html')

    files = ['Book1.xlsx']

    for file in files:
        with open(file, 'rb') as f:
            file_data = f.read()
            file_name = f.name

        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login("touchinvivek@gmail.com", "v8008577345")
        smtp.send_message(msg)
        print('sent..')



schedule.every().day.at("21:28").do(time1)


# Loop so that the scheduling task
# keeps on running all time.
while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)
