# arm core 

pipy部分请参考 <a href="https://github.com/loyaltly-cn/core-setting-server/blob/main/README.md"> core-setting-server </a>

## tips
- `python3 main.py` 会读取物理板的内容 之后会传递给 `core.py`
```python
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
```
- `core.py` 会对所有虚拟键处理处理>
```python
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
```
> 每个虚拟按键触发之后 会先执行 api.py 内的 http请求 返回结果之后会 对程序本身做相应处理

- 请在 core.py 内的 menu function 内做启动音频录制的 command 命令
 ```python
import os
os.system(command)
```
```python
if key == 'start':
        http.createMeeting()
        ws.wsConnect()
    if key == 'end':
        http.closeMeeting()
        ws.handler(key)
        ws.close()
```
> 在此做ffmpeg 的启动和 关闭

- 具体每个虚拟键对应的位数请参考 <a href="https://xinxuemo-images.oss-cn-shanghai.aliyuncs.com/%E6%99%BA%E8%83%BD%E4%BA%A4%E4%BA%92%E7%99%BD%E6%9D%BF%E7%BB%88%E7%AB%AF%E5%9D%90%E6%A0%87%E9%9B%86%E5%BC%80%E5%8F%91%E6%96%87%E6%A1%A3.pdf" target="_blank"> pdf document </a>