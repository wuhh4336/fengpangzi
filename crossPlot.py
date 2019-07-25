# -*- coding:utf8 -*-
#本程序利用散点图展示属性之间得相关性,本程序原书有错误，作者将属性和观察弄混了。

import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot

target_url = ("http://127.0.0.1/merchingLearning/rockVmine/sonar.all-data")

rocksVMines = pd.read_csv(target_url,header = None, prefix = "V")

#计算实数属性间得相关性，这里只考察两次观察——第2次以及第3次为例。

dataRow2 = rocksVMines.iloc[0:60,1]
dataRow3 = rocksVMines.iloc[0:60,2]
plot.scatter(dataRow2,dataRow3)
plot.xlabel("1nd")
plot.ylabel("3rd")
plot.show()

dataRow2 = rocksVMines.iloc[0:60,1]
dataRow21 = rocksVMines.iloc[0:60,21]
plot.scatter(dataRow2,dataRow21)
plot.xlabel("1nd")
plot.ylabel("21rd")
plot.show()
