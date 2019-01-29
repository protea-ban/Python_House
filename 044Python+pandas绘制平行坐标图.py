from numpy import round
from numpy.random import randint, random
from matplotlib.pyplot import legend, show, grid, xticks
import matplotlib.font_manager as fm
from pandas import DataFrame
from pandas.tools.plotting import parallel_coordinates

N = 6
base = randint(100, 120, N)
df = DataFrame({
"姓名": ['运动员' + str(i) for i in range(1, N+1)],
'08岁': base,
'10岁': base+randint(5, 10, N),
'15岁': base+randint(10, 20, N),
'20岁': base+randint(50, 60, N),
'25岁': base+randint(60, 70, N),
})

parallel_coordinates(df, "姓名")
xticks(label=sorted(set(df.columns)-{'姓名'}), fontproperties='simhei')
font = fm.FontProperties(fname=r'C:\Windows\Fonts\STKAITI.ttf')
legend(prop=font, ncol=2)

grid(False)
show()
