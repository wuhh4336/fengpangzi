#coding=utf-8
__author__ = "wuhaohan"
import numpy as np
import pylab
import scipy.stats as stats
import urllib2
import sys

target_url = "http://127.0.0.1/merchingLearning/rockVmine/sonar.all-data"
data = urllib2.urlopen(target_url)
xList = []
labels = []
for line in data:
    row = line.strip().split(',')
    xList.append(row)
nrow = len(xList)
ncol = len(xList[1])
type = [0]*3
colCounters = []
col = 3 #假设绘制第四条属性的图
colData = [] #用来装属性4所有数据的列表
for row in xList:
    colData.append(float(row[col]))#用float变换保证数据格式是浮点型，
stats.probplot(colData,dist='norm',plot=pylab)
pylab.show()


