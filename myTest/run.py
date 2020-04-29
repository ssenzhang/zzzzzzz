#运行检测算法
from greedy import *
from getF import *
M = readData(sys.argv[1])
print("数据读取完成.大小:%d*%d" % (M.shape[0], M.shape[1]))
#lwRes = sqrWeightDown(M)
#lwRes = logWeightDown(M)
lwRes = cubeWeightDown(M)
print(lwRes)
#计算F值
getF11(lwRes)  #无伪装，随机，热门的F值
#getF22(lwRes)  #劫持的F值
#getF33(lwRes)  #分别计算用户和商品的F值
#getF44(lwRes)  #分别计算劫持用户和商品的F值





