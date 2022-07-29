import core
import api as http
import device
import webSocket as ws
import evdev
from evdev import InputDevice,categorize,ecodes

def main():
    dev = InputDevice(device.path)
    x = 0
    flge = True
    for event in dev.read_loop():
        # type == 1 按下和抬起事件
        # value:
        # down == 0
        # up == 1

        if event.type == 1:
            if not event.value:
                flge = True
            ws.touch(event.value)

        if event.type !=4:

            if device.name(event, 'ABS_MT_TOUCH_MAJOR'):
                core.area = event.value

            if device.name(event, 'ABS_X'):
                x = event.value

            if device.name(event, 'ABS_Y'):
                y = event.value
                if not core.coordverify(x,y):
                    core.handler(x, y)
                    if flge:
                        core.handler(x, y)
                        flge = False


if __name__ == '__main__':
    main()
