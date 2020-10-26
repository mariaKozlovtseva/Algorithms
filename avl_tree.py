from binary_search_tree import BinarySearchTree, TreeNode

class AVLtree(BinarySearchTree):
    def _put(self, key, val, curr_node):
        if key < curr_node.key:
            if curr_node.hasLeftChild():
                self._put(key, val, curr_node.leftChild)
            else:
                curr_node.leftChild = TreeNode(key, val, parent=curr_node)
                self.update_balance(curr_node.leftChild)
        else:
            if curr_node.hasRightChild():
                self._put(key, val, curr_node.rightChild)
            else:
                curr_node.rightChild = TreeNode(key, val, parent=curr_node)
                self.update_balance(curr_node.rightChild)

    def update_balance(self, node):
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            return
        if node.parent is not None:
            if node.isLeftChild():
                node.parent.balance_factor += 1
            elif node.isRightChild():
                node.parent.balance_factor -= 1
            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)

    def rebalance(self, node):
        if node.balance_factor < 0:
            if node.rightChild.balance_factor > 0:
                self.rotate_right(node.rightChild)
            self.rotate_left(node)
        elif node.balance_factor > 0:
            if node.leftChild.balance_factor < 0:
                self.rotate_left(node.leftChild)
            self.rotate_right(node)

    def rotate_left(self, rot_root):
        new_root = rot_root.rightChild
        rot_root.rightChild = new_root.leftChild
        if new_root.hasLeftChild:
            new_root.leftChild.parent = rot_root
        new_root.parent = rot_root.parent
        if rot_root.isRoot():
            self.root = new_root
        else:
            if rot_root.isLeftChild():
                rot_root.parent.leftChild = new_root
            else:
                rot_root.parent.rightChild = new_root
        new_root.leftChild = rot_root
        rot_root.parent = new_root
        rot_root.balance_factor = 1 +rot_root.balance_factor - min(0, new_root.balance_factor)
        new_root.balance_factor = 1 + new_root.balance_factor + max(0, rot_root.balance_factor)

    def rotate_right(self, rot_root):
        new_root = rot_root.leftChild
        rot_root.leftChild = new_root.rightChild
        if new_root.hasRightChild():
            new_root.rightChild.parent = rot_root
        new_root.parent = rot_root.parent
        if rot_root.isRoot():
            self.root = new_root
        else:
            if rot_root.isLeftChild():
                rot_root.parent.leftChild = new_root
            else:
                rot_root.parent.rightChild = new_root
        new_root.rightChild = rot_root
        rot_root.parent = new_root
        rot_root.balance_factor = -1 + rot_root.balance_factor - max(0, new_root.balance_factor)
        new_root.balance_factor = -1 + new_root.balance_factor + min(0, rot_root.balance_factor)

if __name__ == '__main__':
    avl = AVLtree()
    avl[3] = 'a'
    avl[2] = 'b'
    avl[4] = 'c'
    avl[0] = 'd'
    avl[2.5] = 'e'
    avl[-1] = 'h'
    # balanced
    print(avl.root.balance_factor)

