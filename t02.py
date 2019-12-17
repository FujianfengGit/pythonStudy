import numpy as np
import matplotlib.pyplot as plt
#产生测试数据
x = np.arange(1,10)
y = x
fig = plt.figure()
plt.scatter(x,y,c = 'r',marker = 'o')  #c = 'r'表示散点的颜色为红色，marker 表示指定三点多形状为圆形
#显示所画的图
plt.show()
