# -*- coding:utf8 -*-

__anthor__ = 'wuhaohan'#非原作者
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot
target_url = ("http://127.0.0.1/merchingLearning/rockVmine/sonar.all-data")

rocksVMines = pd.read_csv(target_url,header = None, prefix = "V")

for i in range(208):
	if rocksVMines.iat[i,60]== "M":
		pcolor = "red"
	else:
		pcolor = "blue"
	#画图
	dataRow = rocksVMines.iloc[i,0:60]
	dataRow.plot(color = pcolor)

plot.xlabel("Attribute index")
plot.ylabel("Attribute Values")
plot.show()

