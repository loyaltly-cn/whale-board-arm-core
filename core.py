import config
import byteHandler
import webSocket as ws
import api as http

area = 0

def coordverify(x,y):
    type = config.getCurrentKey(x,y)
    return not type



def handler(x,y):
    key = config.getCurrentKey(x,y)
    if coordverify(x,y):
        shape = config.getCurrentShape(area)
        byteShape = byteHandler.get(shape)
        data = byteHandler.coord(byteShape,x,y)
        ws.send(data)
    else:
        menu(key)


def menu(key):
    print(key)
    if byteHandler.get(key) > 2 and byteHandler.get(key) < 5:   #penColor
        ws.handler(key)
    if key == 'radio':
        http.radio()
    if key == 'save':
        http.save()
    if key == 'clear':
        ws.handler(key)
    if key == 'start':
        http.createMeeting()
        ws.wsConnect()
    if key == 'end':
        http.closeMeeting()
        ws.handler(key)
        ws.close()






