# -*- coding: utf-8 -*-
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import numpy as np
import matplotlib.pyplot as plt

fs = 20
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=fs)

xmajorLocator = MultipleLocator(0.2)  # 将x主刻度标签设置为0.2的倍数
xmajorFormatter = FormatStrFormatter('%1.1f')  # 设置x轴标签文本的格式
xminorLocator = MultipleLocator(0.1)  # 将x轴次刻度标签设置为0.1的倍数

ymajorLocator = MultipleLocator(0.2)  # 将y轴主刻度标签设置为0.2的倍数
ymajorFormatter = FormatStrFormatter('%1.1f')  # 设置y轴标签文本的格式
yminorLocator = MultipleLocator(0.1)  # 将此y轴次刻度标签设置为0.1的倍数

a = np.linspace(0.02, 0.10, 5)
Z = 1.0 / 3.0

fig, ax = plt.subplots(figsize=(8, 7))

for ii in range(0, 5):
    y = np.linspace(a[ii], 1.0, 200)
    X = (y - a[ii]) / (1.0 - a[ii])
    S_Sa = (((1.0 - y) / y) * (a[ii] / (1.0 - a[ii]))) ** Z
    ax.plot(S_Sa, X)

ax.axis([0, 1.0, 0, 1.0])
plt.title(r'扩散理论的悬移质相对含沙量垂线分布', fontproperties=font)
plt.xlabel(r'相对悬沙浓度$\frac {S} {S_a}$', fontproperties=font)
plt.ylabel(r'距参考点相对高度$\frac {y-a} {h-a} $', fontproperties=font)
legend = ax.legend((r'$\frac {a} {h}=0.02$', r'$\frac {a} {h}=0.04$', r'$\frac {a} {h}=0.06$', r'$\frac {a} {h}=0.08$',
                    r'$\frac {a} {h}=0.10$'), loc='right center', shadow=True, fontsize='x-large')

# Put a nicer background color on the legend.
legend.get_frame().set_facecolor('#00FFCC')

plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
# 设置主刻度标签的位置,标签文本的格式
ax.xaxis.set_major_locator(xmajorLocator)
ax.xaxis.set_major_formatter(xmajorFormatter)

ax.yaxis.set_major_locator(ymajorLocator)
ax.yaxis.set_major_formatter(ymajorFormatter)

# 显示次刻度标签的位置,没有标签文本
ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)

ax.xaxis.grid(True, which='minor')  # x坐标轴的网格使用次刻度
ax.yaxis.grid(True, which='minor')  # y坐标轴的网格使用次刻度
# ax.yaxis.grid(True, which='major') #y坐标轴的网格使用主刻度
ax.grid(color='k', linestyle='-', linewidth=1, alpha=0.2)
plt.subplots_adjust(top=0.90, bottom=0.15, left=0.15, right=0.95)

plt.savefig('a变动.jpg', dpi=300)
plt.show()
