# -*- coding:utf8 -*-
__author__ = 'wuhaohan'
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot
from random import uniform

target_url = ("http://127.0.0.1/merchingLearning/rockVmine/sonar.all-data")

rocksVMines = pd.read_csv(target_url,header=None,prefix = "V") #这里必须用双引号
target = []
for i in range(208):
    if rocksVMines.iat[i,60] == 'M':
        target.append(1.0)
    else:
        target.append(0.0)
plot.figure(1)
dataRow = rocksVMines.iloc[0:208,35] #通过属性直线图发现在属性35处，分类较为明显，这样更能体现对比效果
plot.scatter(dataRow,target)
plot.xlabel("35rdAttribute")
plot.ylabel("target")
plot.show()
#为提高可视化效果#
plot.figure(2)
target = []
for i in range(208):
    if rocksVMines.iat[i,60] == "M":
        target.append(1.0+uniform(-0.1,0.1))
    else:
        target.append(0.0+uniform(-0.1,0.1))

dataRow = rocksVMines.iloc[0:208,35]
plot.scatter(dataRow,target,alpha=0.5,s=120)
plot.xlabel("Attribute Value")
plot.ylabel("Target Value")
plot.show()




