import timeStamp as ts

def get(type):
    if type == 'dowm':
        return 0
    if type == 'up':
        return 1
    if type == 'radio':
        return 2
    if type == 'black':
        return 3
    if type == 'blue':
        return 4
    if type == 'red':
        return 5
    if type == 'save':
        return 6
    if type == 'clear':
        return 7
    if type == 'pen':
        return 8
    if type == 'finger':
        return 9
    if type == 'eraser':
        return 10
    if type == 'start':
        return 11
    if type == 'end':
        return 12

def timeStamp(timeStamp):
    byte1 = timeStamp & 255
    byte2 = timeStamp >> 8 & 255
    byte3 = timeStamp >> 16 & 255
    byte4 = timeStamp >> 24 & 255
    return bytes([byte4, byte3, byte2, byte1])


def coord(shape,x,y):
    xh = x >> 8
    xl = x & 255
    yh = y >> 8
    yl = y & 255
    data = bytes([shape,xh,xl,yh,yl])+timeStamp(ts.nowTimeStamp())
    return  data
