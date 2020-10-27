class BinaryHeap:
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
            if self.heaplist[i] < self.heaplist[i//2]:
                self.swap(i, i//2)
            i //= 2

    def findMin(self):
        return self.heaplist[1]

    def delMin(self, return_min = True):
        self.swap(1, -1)
        result = self.heaplist.pop()
        self.size -= 1
        self.checkPriorityDown(1)
        if return_min:
            return result

    def checkPriorityDown(self, i):
        while i*2 <= self.size:
            min_child = self.minChild(i)
            if self.heaplist[i] > self.heaplist[min_child]:
                self.swap(i, min_child)
            i = min_child

    def minChild(self, i):
        if i*2 + 1 > self.size:
            return i*2
        else:
            if self.heaplist[i*2] < self.heaplist[i*2 + 1]:
                return i*2
            else:
                return i*2 + 1

    def isEmpty(self):
        return True if not self.size else False

    def decrease_key(self, i, new_val):
        self.heaplist[i] = new_val
        self.checkPriorityUp(i)

    def __delitem__(self, i):
        self.decrease_key(i, float('-inf'))
        self.delMin()

    def buildHeap(self, lst):
        self.size = len(lst)
        self.heaplist = [0] + lst[:]
        i = len(lst) // 2
        while i > 0:
            self.checkPriorityDown(i)
            i -= 1

    def heapSort(self, lst):
        self.buildHeap(lst)
        res = []
        while self.size > 1:
            res.append(self.delMin())
        res.append(self.heaplist[-1])
        return res

    def __str__(self):
        return str(self.heaplist)

    def __len__(self):
        return self.size

if __name__ == '__main__':
    bh = BinaryHeap()
    bh.buildHeap([9,6,5,2,3])
    print(len(bh))
    print(bh.findMin())
    print(bh.delMin())
    print(len(bh))
    bh.insert(-5)
    bh.insert(10)
    bh.decrease_key(3, -7)
    print(bh)
    del bh[2]
    print(bh)
    print(len(bh))
    print(bh.heapSort([9,6,5,2,3]))

