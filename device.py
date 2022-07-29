import evdev
from evdev import InputDevice,categorize,ecodes

f = open('/sys/class/net/wlan0/address')
mac = str(f.read()).replace('\n', '')

def name(event,name):
    eventAll = evdev.categorize(event)
    if ecodes.bytype[eventAll.event.type][eventAll.event.code] == name:
        return True

    return False



def getPath():
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        if device.name == 'Uiworks Uiworks Touchscreen':
            return device.path
        elif device.name == 'USBest Technology SiS HID Touch Controller':
            return device.path

path = getPath()