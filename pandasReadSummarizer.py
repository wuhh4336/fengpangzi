# -*- coding:utf8 -*-
__author__="wuhaohan"

import pandas as pd
from pandas import DataFrame
import urllib2
import matplotlib.pyplot as plot#导入matlab画图函数库
target_url = "http://127.0.0.1/merchingLearning/rockVmine/sonar.all-data"
rocksVMines=pd.read_csv(target_url,header =None,prefix = 'V')
print(rocksVMines.head())#dataFrame.head()显示头n（默认5）列
print(rocksVMines.tail())#dataFrame.head()显示尾n（默认5）列
summary = rocksVMines.describe()# DataFrame.describe()显示整改DataFrame属性的统计特性。输出也已数据框DataFrame的形式展示
print(summary)


