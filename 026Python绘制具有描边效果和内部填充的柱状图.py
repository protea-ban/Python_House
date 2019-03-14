import numpy as np
import matplotlib.pyplot as plt
#生成测试数据
x = np.linspace(0, 10, 11)
y = 11 - x

plt.bar(x,
        y,
        color = '#772277',
        alpha = 0.5,
        edgecolor = 'blue',
        linestyle = '--',
        linewidth = 1,
        hatch='*')

# 为每个柱形添加文本标注
for xx, yy in zip(x, y):
    plt.text(xx-0.2, yy+0.1, '%2d' % yy)

plt.show()
