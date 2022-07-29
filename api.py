import requests as http
import timeStamp as ts
#import device

slbApi = 'https://api.bj-jiuqi.com/slbApi/'
armApi = 'https://api.bj-jiuqi.com/armApi/'

ws = http.post(slbApi+'slbs').text

#mac = device.mac
mac = '12:81:5e:e4:2b:4b'


token = http.post(armApi+'deviceAuth',data={"mac":mac}).json()['data']
did = http.post(armApi+'deviceDPQM',data={"mac":mac,"token":token}).json()['data'][0]['id']
currentMid = -1

def createMeeting():
    res = http.post(armApi+'meetings',data={"url":ws,"did":did,"token":token}).json()
    global currentMid
    currentMid = res['data']

def radio():
    http.put(armApi+'meetings',data={"token":token,"state":True,"id":currentMid})

def save():
    http.post(armApi+'snapShots',data={"token":token,"timeStamp":ts.nowTimeStamp(),"mid":currentMid})

def closeMeeting():
    print('close meeting')
    http.put(armApi+'meetings',data={"token":token,"state":False,"id":currentMid})

def getMeetingWs():
    res = http.post(armApi+'/meetingDPQM',data={"token":token,"id":currentMid}).json()['data'][0]
    return res['url']
