class Node:
    size = 0
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        if not self.tail:
            self.setHead(node)
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if not node.prev:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if not node.next:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        """
        :param position: count starts at 0
        :param nodeToInsert: object of class Node

        """
        if position == 0:
            self.setHead(nodeToInsert)
        node = self.head
        count = 0
        while count != position:
            node = node.next
            count += 1
        if not node:
            self.setTail(nodeToInsert)
        else:
            self.insertBefore(node,nodeToInsert)

    def removeNodesWithValue(self, value):
        node = self.head
        val = node.value
        while val != value:
            node = self.head.next
            val = node.value
        self.remove(node)

    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None
