class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        current_node = self
        while True:
            if value < current_node.value:
                if current_node.right is None:
                    current_node.right = BST(value)
                    break
                else:
                    current_node = current_node.right
            else:
                if current_node.left is None:
                    current_node.left = BST(value)
                    break
                else:
                    current_node = current_node.left
        return self

    def delete(self, value, parent=None):
        current_node = self
        while current_node is not None:
            if value < current_node.value:
                parent = current_node
                current_node = current_node.right
            elif value > current_node.value:
                parent = current_node
                current_node = current_node.left
            else:
                if current_node.left is not None and current_node.right is not None:
                    current_node.value = current_node.right.min_value()
                    current_node.right.delete(current_node.value, current_node)

                elif not parent:
                    if current_node.left is not None:
                        current_node.value = current_node.left.value
                        current_node.right = current_node.left.right
                        current_node.left = current_node.left.left
                    elif current_node.right is not None:
                        current_node.value = current_node.right.value
                        current_node.right = current_node.right.right
                        current_node.left = current_node.right.left
                    else:
                        pass
                elif parent.left == current_node:
                    parent.left = current_node.left if current_node.left is not None else current_node.right
                elif parent.right == current_node:
                    parent.right = current_node.left if current_node.left is not None else current_node.right
                break
        return self

    def min_value(self):
        current_node = self
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def search(self, value):
        current_node = self
        contains = False
        while current_node is not None:
            if value == current_node.value:
                contains = True
                break
            elif value > current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return contains

if __name__ == '__main__':
    tree = BST(5)
    tree.insert(10)
    tree.insert(20)
    tree.insert(-2)
    print(tree.search(-2))
    tree.delete(20)