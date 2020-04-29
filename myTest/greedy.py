#采用贪心的思想检测矩阵中最密集的区域
import numpy as np
import sys
from scipy import sparse
from PrHeap import PrHeap
# np.set_printoptions(threshold=1000000000)
# np.set_printoptions(linewidth=160)

#返回稀疏矩阵
def listToSparseMatrix(edgesSource, edgesDest):
    m = max(edgesSource) + 1
    n = max(edgesDest) + 1
    M = sparse.coo_matrix(([1]*len(edgesSource), (edgesSource, edgesDest)), shape=(m, n))
    M1 = M > 0
    return M1.astype('int')
#读取数据
def readData(filename):
    edgesSource = []
    edgesDest = []
    with open(filename) as f:
        for line in f:
            toks = line.split(',')
            edgesSource.append(int(toks[0]))
            edgesDest.append(int(toks[1]))
    return listToSparseMatrix(edgesSource, edgesDest)
def c2Score(M, rowSet, colSet, nodeSusp):
    suspTotal = nodeSusp[0][list(rowSet)].sum() + nodeSusp[1][list(colSet)].sum()
    return M[list(rowSet),:][:,list(colSet)].sum(axis=None) + suspTotal
#平方根降权
def sqrWeightDown(M, nodeSusp=None):
    (m, n) = M.shape
    colSums = M.sum(axis=0)
    colWeights = np.squeeze(np.array(1.0 / np.sqrt((np.squeeze(colSums) + 5))))
    colDiag = sparse.lil_matrix((n, n))
    colDiag.setdiag(colWeights)
    W = M * colDiag
    print("权重矩阵计算完成.")
    return fastGreedyDecreasing(W, colWeights, nodeSusp)
#log降权
def logWeightDown(M, nodeSusp=None):
    (m, n) = M.shape
    colSums = M.sum(axis=0)
    colWeights = 1.0 / np.squeeze(np.array(np.log((np.squeeze(colSums) + 5))))
    colDiag = sparse.lil_matrix((n, n))
    colDiag.setdiag(colWeights)
    W = M * colDiag
    print("权重矩阵计算完成.")
    return fastGreedyDecreasing(W, colWeights, nodeSusp)
#立方根降权
def cubeWeightDown(M, nodeSusp=None):
    (m, n) = M.shape
    colSums = M.sum(axis=0)
    A=np.array(colSums)
    colWeights = np.squeeze(np.array(1.0/pow(A+5,1.0/3)))
    colDiag = sparse.lil_matrix((n, n))
    colDiag.setdiag(colWeights)
    W = M * colDiag
    print("权重矩阵计算完成.")
    return fastGreedyDecreasing(W, colWeights, nodeSusp)

def fastGreedyDecreasing(M, colWeights, nodeSusp=None):
    (m, n) = M.shape
    if nodeSusp is None:
        nodeSusp = (np.zeros(m), np.zeros(n))
    Md = M.todok()
    Ml = M.tolil()
    Mlt = M.transpose().tolil()
    rowSet = set(range(0, m))
    colSet = set(range(0, n))
    curScore = c2Score(M, rowSet, colSet, nodeSusp)

    bestAveScore = curScore / (len(rowSet) + len(colSet))
    bestSets = (rowSet, colSet)
    print("初始化完成.")
    rowDeltas = np.squeeze(M.sum(axis=1).A) + nodeSusp[0]  #行权重
    colDeltas = np.squeeze(M.sum(axis=0).A) + nodeSusp[1]  #列权重
    print("增量设置完成.")
    rowTree = PrHeap(rowDeltas)
    colTree = PrHeap(colDeltas)
    print("堆构建完成.")

    numDeleted = 0
    deleted = []
    bestNumDeleted = 0

    while rowSet and colSet:
        if (len(colSet) + len(rowSet)) % 100000 == 0:
            print("目前集合大小 = %d" % (len(colSet) + len(rowSet),))
        (nextRow, rowDelt) = rowTree.getMin()
        (nextCol, colDelt) = colTree.getMin()
        if rowDelt <= colDelt:
            curScore -= rowDelt
            for j in Ml.rows[nextRow]:
                delt = colWeights[j]
                colTree.changeVal(j, -colWeights[j])
            rowSet -= {nextRow}
            rowTree.changeVal(nextRow, float('inf'))
            deleted.append((0, nextRow))
        else:
            curScore -= colDelt
            for i in Mlt.rows[nextCol]:
                delt = colWeights[nextCol]
                rowTree.changeVal(i, -colWeights[nextCol])
            colSet -= {nextCol}
            colTree.changeVal(nextCol, float('inf'))
            deleted.append((1, nextCol))

        numDeleted += 1
        curAveScore = curScore / (len(colSet) + len(rowSet))

        if curAveScore > bestAveScore:
            bestAveScore = curAveScore
            bestNumDeleted = numDeleted

    # 重建最佳的行和列集合
    finalRowSet = set(range(m))
    finalColSet = set(range(n))
    for i in range(bestNumDeleted):
        if deleted[i][0] == 0: 
            finalRowSet.remove(deleted[i][1])
        else:
            finalColSet.remove(deleted[i][1])
    return ((finalRowSet, finalColSet), bestAveScore)
def addNodeSuspicious(M):
    rowSusp = np.loadtxt("%s.rows" % (sys.argv[3],))
    colSusp = np.loadtxt("%s.cols" % (sys.argv[3],))
    lwRes = logWeightDown(M, (rowSusp, colSusp))
    print(lwRes)