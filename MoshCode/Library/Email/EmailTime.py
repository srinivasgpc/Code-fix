import datetime as dt
import time
import schedule
import smtplib

def send_email():
    print('email sent')
    #email_user = 'kasturi.vivek994@gmail.com'
    email_user = 'srinivasgaddam423@gmail.com'
    server = smtplib.SMTP ('smtp.gmail.com', 587)
    server.starttls()
    server.login("touchinvivek@gmail.com", "v8008577345")

    #EMAIL
    message = 'sending this from python!'
    server.sendmail(email_user, email_user, message)
    server.quit()


send_time = dt.datetime(2020,4,30,20,36,0) # set your sending time in UTC
time.sleep(send_time.timestamp() - time.time())


schedule.every().day.at("21:11").do(send_email)

