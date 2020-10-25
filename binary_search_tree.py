class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
       self.key = key
       self.payload = val
       self.leftChild = left
       self.rightChild = right
       self.parent = parent
       self.balance_factor = 0

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __setitem__(self, key, val):
        if not self.root:
            self.root = TreeNode(key, val)
        else:
            self._put(key, val, self.root)
        self.size += 1

    def _put(self, key, val, curr_node):
        if key < curr_node.key:
            if curr_node.hasLeftChild():
                self._put(key, val, curr_node.leftChild)
            else:
                curr_node.leftChild = TreeNode(key, val, parent=curr_node)
        elif key == curr_node.key:
            curr_node.payload = val
        else:
            if curr_node.hasRightChild():
                self._put(key, val, curr_node.rightChild)
            else:
                curr_node.rightChild = TreeNode(key, val, parent=curr_node)

    def __getitem__(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        return None

    def _get(self, key, curr_node):
        if not curr_node:
            return None
        elif key == curr_node.key:
            return curr_node
        elif key < curr_node.key:
            return self._get(key, curr_node.leftChild)
        else:
            return self._get(key, curr_node.rightChild)

    def __len__(self):
        return self.size

    def __delitem__(self, key):
        if self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        elif self.size > 1:
            node = self._get(key, self.root)
            if node:
                self.remove(node)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        else:
            raise KeyError('Error, key not in tree')

    def remove(self, node):
        if node.isLeaf():
           if node.parent.leftChild == node:
               node.parent.leftChild = None
           else:
               node.parent.rightChild = None
        elif node.hasBothChildren():
            succ = self.findSuccessor(node)
            self.unite(succ)
            node.key = succ.key
            node.payload = succ.payload
        else:
            if node.hasLeftChild():
                if node.isLeftChild():
                    node.leftChild.parent = node.parent
                    node.parent.leftChild = node.leftChild
                elif node.isRightChild():
                    node.leftChild.parent = node.parent
                    node.parent.rightChild = node.leftChild
                else:
                    node.replcaNodeData(node.leftChild.key, node.leftChild.payload,
                                        node.leftChild.leftChild, node.leftChild.rightChild)
            else:
                if node.isLeftChild():
                    node.rightChild.parent = node.parent
                    node.parent.leftChild = node.rightChild
                elif node.isRightChild():
                    node.rightChild.parent = node.parent
                    node.parent.rightChild = node.rightChild
                else:
                    node.replcaNodeData(node.rightChild.key, node.rightChild.payload,
                                        node.rightChild.leftChild, node.rightChild.rightChild)

    def findSuccessor(self, node):
        succ = None
        if node.hasRightChild():
            succ = self.findMin(node.rightChild)
        else:
            if node.parent:
                if node.isLeftChild():
                    succ = node.parent
                else:
                    node.parent.rightChild = None
                    succ = self.findSuccessor(node.parent)
                    node.parent.rightChild = self
        return succ

    def findMin(self, node):
        curr = node
        while curr.hasLeftChild():
            curr = curr.leftChild
        return curr

    def unite(self, node):
        if node.isLeaf():
            if node.isLeftChild():
                node.parent.leftChild = None
            else:
                node.parent.rightChild = None
        elif node.hasAnyChildren():
            if node.hasLeftChild():
                if node.isLeftChild:
                    node.parent.leftChild = node.leftChild
                else:
                    node.parent.rightChild = node.leftChild
                node.leftChild.parent = node.parent
            else:
                if node.isLeftChild:
                    node.parent.leftChild = node.rightChild
                else:
                    node.parent.rightChild = node.rightChild
                node.rightChild.parent = node.parent

    def __contains__(self, key):
        if self[key]: return True


if __name__ == '__main__':
    mytree = BinarySearchTree()
    mytree[3] = "red"
    mytree[1] = "blue"
    mytree[6] = "yellow"
    mytree[2] = "at"
    mytree[-2] = "hello"
    mytree[0] = "world"
    print(mytree[6])
    print(mytree[2])
    mytree[6] = 'green'
    print(mytree[6])
    print(10 in mytree)
    print(len(mytree))
    del mytree[1]
    print(len(mytree))