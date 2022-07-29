import byteHandler
import timeStamp as ts
import websocket
import api as http

websocket.enableTrace(True)
ws = websocket.WebSocket()
flge = False

def wsConnect():
    global flge
    if not flge:
        url = 'wss://'+http.getMeetingWs()+'/'+str(http.currentMid)+'/'+'main/'
        ws.connect(url, origin="testing_websockets.com")
        flge = True
        data = bytes([byteHandler.get('start')]) + byteHandler.timeStamp(ts.nowTimeStamp())
        send(data)

def send(data):
    #print(data)
    global flge
    if flge:
        ws.send(data, websocket.ABNF.OPCODE_BINARY)

def handler(types):

    type = byteHandler.get(types)
    data = bytes([type]) + byteHandler.timeStamp(ts.nowTimeStamp())
    send(data)

def touch(types):
    data = bytes([types]) + byteHandler.timeStamp(ts.nowTimeStamp())
    send(data)

def close():
    global flge
    if flge:
        data = bytes([byteHandler.get('end')]) + byteHandler.timeStamp(ts.nowTimeStamp())
        send(data)
        flge = False
        ws.close()



