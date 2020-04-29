import numpy as np
import random
import pandas as pd
import csv
from collections import Counter

#读取原文件
list1=[];list2=[]
sFileName='amazonData0.004.csv'
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

#劫持正常用户
def func4(density):
    hijackedCol1=[];hijackedCol2=[]
    # #去重
    setHijacked = list(set(list1));setHijacked.sort(key=list1.index)
    # #在正常用户中随机选出200个作为挟持对象
    hijacked=random.sample(setHijacked,200)
    for i in hijacked:
        for j in range(2001,2201):
            if(random.random()<density):
                print(i,j)
                hijackedCol1.append(i)
                hijackedCol2.append(j)
    dataframe = pd.DataFrame({"":hijacked})
    dataframe.to_csv("目标%.3f.csv"%(density), index=False, sep=',',header=0)
    dataframe = pd.DataFrame({'fakeUser': hijackedCol1, 'hotGoods': hijackedCol2})
    dataframe.to_csv("%.3f劫持用户.csv"%(density), index=False, sep=',',header=0)
#生成子图文件
densityList=[0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.046,0.047,0.048,0.049,0.050,0.055,0.06,0.065,0.07,0.075,0.08,0.085,0.09,0.095,0.10,0.105,0.11,0.115,0.12]
def fileCopy():
    for i in range(0, len(densityList)):
        # 原始数据
        with open('劫持用户%.3f.csv' % (densityList[i]), 'ab') as f:
            f.write(open('amazonData0.0016.csv', 'rb').read())
            # os.rename('test.csv','劫持用户%.3f.csv'%(densityList[i]))
fileCopy()
for i in range(0,len(densityList)):
    func4(densityList[i])
    #合成一张图
    with open('劫持用户%.3f.csv' % (densityList[i]), 'ab') as f:
        f.write(open('%.3f劫持用户.csv'%(densityList[i]),'rb').read())
        # os.rename('test.csv','劫持用户%.3f.csv'%(densityList[i]))

#with open('1.csv','ab') as f:
#f.write(open('2.csv','rb').read())#将2.csv内容追加到1.csv的后面