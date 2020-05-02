from datetime import datetime, timedelta
from time import time

#time delt uses to add the
dt1 = datetime(2018, 1, 1) + timedelta(days =1, seconds =1)#
dt2 = datetime.now() # present time
dt =datetime.strptime("2018/01/01", "%Y/%m/%d")#time denotion
dt = datetime.fromtimestamp(time())
print(dt)

print(f"{dt.year}/{dt.month}")# in other way

print(dt.strftime("%Y/%m"))
print(dt1>dt2)#returns false

duration = dt2 -dt1
print(duration)
print("days", duration.days)
print("seconds", duration.seconds)
print("total_seconds", duration.total_seconds())