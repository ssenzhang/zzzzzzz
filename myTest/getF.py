import csv
import sys
import pandas as pd

#无伪装，随机，伪装热门三种情况的F值
def getF11(lwRes):
	preUserList=list(lwRes[0][0]);preGoodsList=list(lwRes[0][1])
	userPreTrue=0;goodsPreTrue=0
	for x in preUserList:
		if x in range(2001,2201):
			userPreTrue+=1
	for x in preGoodsList:
		if x in range(2001,2201):
			goodsPreTrue+=1
	P=(userPreTrue+goodsPreTrue)/(len(preUserList)+len(preGoodsList))
	R=(userPreTrue+goodsPreTrue)/400
	if P==0 and R==0:
		F=0
	else:
		F=(2*P*R)/(P+R)

	tmp=[]
	tmp.append(F)
	dataframe = pd.DataFrame({'F值':tmp})
	dataframe.to_csv("每次F值.csv", index=False, sep=',',header=0)
	with open('F值.csv' , 'ab') as f:
		f.write(open('每次F值.csv', 'rb').read())
	print("P=%f"%(P),"R=%f"%(R),"F=%f"%(F))

#劫持用户F值
def getF22(lwRes):
	str=sys.argv[1][9:14]
	sFileName = '目标%s.csv'%(str)
	hijacked = []
	with open(sFileName, newline='', encoding='UTF-8') as csvfile:
		rows = csv.reader(csvfile)
		for row in rows:
			hijacked.append(row[0])
	hijacked = list(map(int, hijacked))

	preUserList = list(lwRes[0][0])
	preGoodsList = list(lwRes[0][1])
	userPreTrue = 0;goodsPreTrue = 0
	for x in preUserList:
		if x in hijacked:
			userPreTrue += 1
	for x in preGoodsList:
		if x in range(2001, 2201):
			goodsPreTrue += 1
	P = (userPreTrue + goodsPreTrue) / (len(preUserList) + len(preGoodsList))
	R = (userPreTrue + goodsPreTrue) / 400
	if P == 0 and R == 0:
		F = 0
	else:
		F = (2 * P * R) / (P + R)
	tmp = []
	tmp.append(F)
	dataframe = pd.DataFrame({'F值': tmp})
	dataframe.to_csv("每次F值.csv", index=False, sep=',', header=0)
	with open('F值.csv', 'ab') as f:
		f.write(open('每次F值.csv', 'rb').read())
	print("P=%f" % (P), "R=%f" % (R), "F=%f" % (F))

#计算前三种用户和商品F值
def getF33(lwRes):
	preUserList=list(lwRes[0][0]);preGoodsList=list(lwRes[0][1])
	userPreTrue=0;goodsPreTrue=0
	for x in preUserList:
		if x in range(2001,2201):
			userPreTrue+=1
	for x in preGoodsList:
		if x in range(2001,2201):
			goodsPreTrue+=1
	P1=userPreTrue/len(preUserList)
	R1=userPreTrue/200
	P2=goodsPreTrue/len(preGoodsList)
	R2=goodsPreTrue/200
	if P1==0 and R1==0:
		F1=0
	else:
		F1=(2*P1*R1)/(P1+R1)
	if P2==0 and R2==0:
		F2=0
	else:
		F2=(2*P2*R2)/(P2+R2)
	print("F1:%f"%(F1),"F2:%f"%(F2))

#计算劫持用户和者商品的F值
def getF44(lwRes):
	str = sys.argv[1][9:14]
	print(str)
	sFileName = '目标%s.csv' % (str)
	hijacked = []
	with open(sFileName, newline='', encoding='UTF-8') as csvfile:
		rows = csv.reader(csvfile)
		for row in rows:
			hijacked.append(row[0])
	hijacked = list(map(int, hijacked))

	preUserList = list(lwRes[0][0])
	preGoodsList = list(lwRes[0][1])
	userPreTrue = 0
	goodsPreTrue = 0
	for x in preUserList:
		if x in hijacked:
			userPreTrue += 1
	for x in preGoodsList:
		if x in range(2001, 2201):
			goodsPreTrue += 1
	P1 = userPreTrue / len(preUserList)
	R1 = userPreTrue / 200
	P2 = goodsPreTrue / len(preGoodsList)
	R2 = goodsPreTrue / 200
	if P1 == 0 and R1 == 0:
		F1 = 0
	else:
		F1 = (2 * P1 * R1) / (P1 + R1)
	if P2 == 0 and R2 == 0:
		F2 = 0
	else:
		F2 = (2 * P2 * R2) / (P2 + R2)
	print("F1:%f" % (F1), "F2:%f" % (F2))
