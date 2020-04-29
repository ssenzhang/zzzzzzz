
#一个树数据结构，它存储度数列表并可以快速检索最小度数元素，
#或修改任何度数，每个度数都是对数时间。 它通过使用
#给定叶子中的元素，每个内部节点存储两个孩子的最小值。
import math
class PrHeap:
    def __init__(self, degrees):
        self.height = int(math.ceil(math.log(len(degrees), 2)))
        self.numLeaves = 2 ** self.height
        self.numBranches = self.numLeaves - 1
        self.n = self.numBranches + self.numLeaves
        self.nodes = [float('inf')] * self.n
        for i in range(len(degrees)):
            self.nodes[self.numBranches + i] = degrees[i]
        for i in reversed(range(self.numBranches)):
            self.nodes[i] = min(self.nodes[2 * i + 1], self.nodes[2 * i + 2])

    def getMin(self):
        cur = 0
        for i in range(self.height):
            cur = (2 * cur + 1) if self.nodes[2 * cur + 1] <= self.nodes[2 * cur + 2] else (2 * cur + 2)
        # print "found min at %d: %d" % (cur, self.nodes[cur])
        return (cur - self.numBranches, self.nodes[cur])

    def changeVal(self, idx, delta):
        cur = self.numBranches + idx
        self.nodes[cur] += delta
        for i in range(self.height):
            cur = (cur - 1) // 2
            nextParent = min(self.nodes[2 * cur + 1], self.nodes[2 * cur + 2])
            if self.nodes[cur] == nextParent:
                break
            self.nodes[cur] = nextParent

    def dump(self):
        print ("numLeaves: %d, numBranches: %d, n: %d, nodes: " % (self.numLeaves, self.numBranches, self.n))
        cur = 0
        for i in range(self.height + 1):
            for j in range(2 ** i):
                print (self.nodes[cur],)
                cur += 1
            print( '')
