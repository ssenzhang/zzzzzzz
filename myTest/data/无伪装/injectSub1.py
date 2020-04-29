import numpy as np
import random
import pandas as pd
import csv
from collections import Counter

#读取原文件
list1=[];list2=[]
sFileName='amazonData0.004.csv'
#sFileName='amazonData0.0016.csv'
#sFileName='test.csv'
with open(sFileName,newline='',encoding='UTF-8') as csvfile:
    rows=csv.reader(csvfile)
    for row in rows:
        list1.append(row[0])    #读第一列
        list2.append(row[1])    #读第二列
#['1','2']to[1,2]
list1=list(map(int,list1));list2=list(map(int,list2))   #不用list得到的是迭代器
maxUserNode=max(list1);maxGoodsNode=max(list2)          #最大的用户和商品
print("最大用户%d"%maxUserNode,"最大商品%d"%maxGoodsNode)
# doc = open('noRandom.txt', 'a')  # 打开创建好的1.txt文件，参数a表示：打开写入，如果存在，则附加到文件的末尾
#print("New", file=doc)
#无伪装

def func1(density):
  nonListcol1=[];nonListcol2=[]
  for i in range(2001,2201):
      for j in range(2001,2201):
          if(random.random()<density):
             print(i,j)
             nonListcol1.append(i)
             nonListcol2.append(j)
             # print(i,j, file=doc)
  dataframe = pd.DataFrame({'User': nonListcol1, 'Goods': nonListcol2})
  # 将DataFrame存储为csv,index表示是否显示行名，default=True不显示
  dataframe.to_csv("%.3f无伪装.csv"%(density), index=False, sep=',',header=0)
densityList=[0.01,0.015,0.02,0.025,0.03,0.035,0.036,0.037,0.038,0.039,0.04,0.045,0.046,0.047,0.048,0.049,0.050,0.055,0.06,0.065,0.07,0.075,0.08,0.085,0.09,0.095,0.10,0.105,0.11,0.115,0.12]
def copyFile():
    for i in range(0, len(densityList)):
        # 原始数据
        with open('无伪装%.3f.csv' % (densityList[i]), 'ab') as f:
            f.write(open('amazonData0.004.csv', 'rb').read())
            # os.rename('test.csv','劫持用户%.3f.csv'%(densityList[i]))
def funInsertWu():
    for i in range(0,len(densityList)):
        func1(densityList[i])
        with open('无伪装%.3f.csv' % (densityList[i]), 'ab') as f:
            f.write(open('%.3f无伪装.csv'%(densityList[i]),'rb').read())
copyFile()
funInsertWu()