__author__ = 'wuhaohan'
import urllib2
import sys
#read data from
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")
data = urllib2.urlopen(target_url)
#arrage data into list for labels amd list of lists for attributes
xList=[]
labels=[]
for line in data:
    row = line.strip().split(",")
    xList.append(row)
sys.stdout.write("Number os Rows of data = "+str(len(xList))+'\n')
sys.stdout.write("Number os Rows of data = "+str(len(xList[1]))+'\n')
