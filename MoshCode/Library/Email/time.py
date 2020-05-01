# Schedule Library imported
import schedule
import time
import smtplib

# Functions setup



def bedtime():
    print("It is bed time go rest")
    # email_user = 'kasturi.vivek994@gmail.com'
    email_user = 'srinivasgaddam423@gmail.com'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("touchinvivek@gmail.com", "v8008577345")

    # EMAIL
    message = 'sending this from python!'
    server.sendmail(email_user, email_user, message)
    server.quit()





# Every day at 12am or 00:00 time bedtime() is called.
schedule.every().day.at("21:14").do(bedtime)


# Loop so that the scheduling task
# keeps on running all time.
while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)
