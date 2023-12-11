

import datetime

#1
now = datetime.datetime.now()
print(now)
print("------")
#2
five_days =(now - datetime.timedelta(days=5))

print(now - five_days)
print("------")
#3

print(now + datetime.timedelta(hours=8))
print("------")
#4
print(now.strftime("%Y %m %d, %X"))
print(now.strftime("%x"))
