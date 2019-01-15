"""
1. 手机已经打开GPS
2. 在安卓手机上安装QPython3
3. 使用编辑器编写下面的代码。
"""

from time import sleep
from androidhelper import Android

# 创建一个实例对象
d = Android()
# 开始读取数据
d.startLocating()

while True:
    data = d.getLastKnownLocation()
    data = data.result

    if data:
        print(data['gps'])
    else:
        print('no gps')

    sleep(5)

# 停止读取数据
d.stopLocating()
