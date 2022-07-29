import time
import datetime

def zeroTimeStamp():
    timeStamp = int(time.mktime(time.strptime(datetime.datetime.now().strftime("%Y-%m-%d"), "%Y-%m-%d")))
    timeStamp = int(str(timeStamp) + '000')
    return timeStamp

zero = zeroTimeStamp()

def nowTimeStamp():
    nowMicroTimeStamp = int(round(time.time() * 1000))
    return nowMicroTimeStamp - zero

