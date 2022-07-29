import json

path = './config.json'

def readFile():
    with open(path,'r',encoding='utf-8') as f:
        data = json.load(f)
        return data

fileInfo = readFile()
keys = fileInfo['virtualKey'].items()
shapes = fileInfo['shapeType']

def getCurrentKey(x,y):
    for key,value in keys:
        if x > value['ax'] and x < value['bx'] and y > value['ay'] and y < value['by']:
            return key

    return False

def getCurrentShape(data):
    if data >= shapes['eraser']:
        return  'eraser'

    return 'pen'

