class MaxBinaryHeap:
    def __init__(self):
        self.heaplist = [0]
        self.size = 0

    def insert(self, k):
        self.heaplist.append(k)
        self.size += 1
        self.checkPriorityUp()

    def swap(self, i, j):
        self.heaplist[i], self.heaplist[j] = self.heaplist[j], self.heaplist[i]
        return self

    def checkPriorityUp(self, i=0):
        if not i: i = self.size
        while i//2:
            if self.heaplist[i] > self.heaplist[i//2]:
                self.swap(i, i//2)
            i //= 2

    def findMax(self):
        return self.heaplist[1]

    def delMax(self, return_max = True):
        self.swap(1, -1)
        result = self.heaplist.pop()
        self.size -= 1
        self.checkPriorityDown()
        if return_max:
            return result

    def checkPriorityDown(self, i=1):
        while i*2 <= self.size:
            max_child = self.maxChild(i)
            if self.heaplist[i] < self.heaplist[max_child]:
                self.swap(i, max_child)
            i = max_child

    def maxChild(self, i):
        if i*2 + 1 > self.size:
            return i*2
        else:
            if self.heaplist[i*2] > self.heaplist[i*2 + 1]:
                return i*2
            else:
                return i*2 + 1

    def isEmpty(self):
        return True if not self.size else False

    def __str__(self):
        return str(self.heaplist)

    def __len__(self):
        return self.size

if __name__ == '__main__':
    max_bh = MaxBinaryHeap()
    n_oper = int(input())
    for i in range(n_oper):
        oper_num = input().split(' ')
        if oper_num[0][0] == 'I':
            max_bh.insert(int(oper_num[1]))
        else:
            print(max_bh.delMax(return_max=True))
