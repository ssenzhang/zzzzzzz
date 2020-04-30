import csv
import random
import networkx as nx

sFilename = "data/ratings_Amazon_Instant_Video.csv"
#从数据集中随机采取2000个用户节点和2000个商品节点
def sample():
    list1 = []
    list2 = []
    with open(sFilename, encoding='utf-8') as f:
        col = 0
        for row in csv.reader(f):
            list1.append(row[0])
            list2.append(row[1])
            col += 1
        print("total cols: ", col)
    #去重
    set1 = list(set(list1))
    set2 = list(set(list2))
    print("The sum of user node: ", len(set1))
    print("The sum of goods node: ", len(set2))
    print()

    popularUsers = []  # 10
    popularGoods = []  # 200
    #创建无向图
    G = nx.Graph()
    #加边
    G.add_edges_from(zip(list1, list2))
    #选高度用户节点
    for i in range(len(set1)):
        if len(list(G.neighbors(set1[i]))) > 20:
            popularUsers.append(set1[i])
    #选高度商品节点
    for i in range(len(set2)):
        if len(list(G.neighbors(set2[i]))) > 250:
            popularGoods.append(set2[i])
    print("user wise degree > 20: ", len(popularUsers))
    print("good wise degree > 200: ", len(popularGoods))

    pickUsers = []
    pickGoods = []
    pickUsers.extend(popularUsers)
    pickGoods.extend(popularGoods)
    leftUsers = set(set1) - set(pickUsers)
    leftGoods = set(set2) - set(pickGoods)
    #选剩余的节点
    for time in range(100):
        pickUsers.extend(random.sample(leftUsers, 2000 - len(pickUsers)))
        pickGoods.extend(random.sample(leftGoods, 2000 - len(pickGoods)))

        pickUsersSet = set()
        pickGoodsSet = set()
        count = 0
        for i in range(len(list1)):
            if list1[i] in pickUsers and list2[i] in pickGoods:
                pickUsersSet.add(list1[i])
                pickGoodsSet.add(list2[i])
                count += 1
        print("total picked users at time " + str(time + 1) + " : ", len(pickUsersSet))
        print("total picked goods at time " + str(time + 1) + " : ", len(pickGoodsSet))
        print("total picked edges at time " + str(time + 1) + " : ", count)

        if (len(pickUsersSet) == 2000 and len(pickGoodsSet) == 2000):
            break

        pickUsers = list(pickUsersSet)
        pickGoods = list(pickGoodsSet)
        leftUsers = set(set1) - pickUsersSet
        leftGoods = set(set2) - pickGoodsSet

    f = open("data/sample.csv", "w")
    for i in range(len(list1)):
        if list1[i] in pickUsers and list2[i] in pickGoods:
            f.write(list1[i] + "," + list2[i] + "\n")
            f.flush()
    f.close()

#编码成数字0到2000
def recode():
    list1 = []
    list2 = []
    with open("data/sample.csv", encoding='utf-8') as f:
        col = 0
        for row in csv.reader(f):
            list1.append(row[0])
            list2.append(row[1])
            col += 1
        print("total cols: ", col)
    print(list1)
    print(list2)

    set1 = list(set(list1))
    set1.sort(key=list1.index)
    set2 = list(set(list2))
    set2.sort(key=list2.index)
    print(len(set1))
    print(len(set2))

    f = open("data/sample_recode.csv", "w")
    for i in range(len(list1)):
        f.write(str(set1.index(list1[i])) + "," + str(set2.index(list2[i])) + "\n")
        f.flush()
    f.close()

if __name__ == '__main__':
    sample()
    recode()
