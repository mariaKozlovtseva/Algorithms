class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def postfix_string(s):
    s = s.split()
    priority = {'(': 0, '-':1, '+':1, '*':2, '/':2}
    stack = Stack()
    result = []
    for elem in s:
        if elem in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or elem in "0123456789":
            result.append(elem)
        elif elem == '(': stack.push(elem)
        elif elem == ')':
            top_el = stack.pop()
            while top_el != '(':
                result.append(top_el)
                top_el = stack.pop()
        else:
            while not stack.isEmpty() and priority[stack.peek()] > priority[elem]:
                result.append(stack.pop())
            stack.push(elem)
    while not stack.isEmpty():
        result.append(stack.pop())
    return ' '.join(result)


def prefix_string(s):
    s = s.split()
    priority = {')': 0, '-': 1, '+': 1, '*': 2, '/': 2}
    result = []
    stack = Stack()
    for elem in s[::-1]:
        if elem in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or elem in "0123456789":
            result.insert(0, elem)
        elif elem == ')':
            stack.push(elem)
        elif elem == '(':
            top_el = stack.pop()
            while top_el != ')':
                result.insert(0, top_el)
                top_el = stack.pop()
        else:
            if not stack.isEmpty() and priority[stack.peek()] > priority[elem]:
                result.insert(0, stack.pop())
            stack.push(elem)
    while not stack.isEmpty():
        result.insert(0,stack.pop())
    return ' '.join(result)

if __name__ == '__main__':
    print(postfix_string("( A + B ) * C - ( D - E ) * ( F + G )"))
    print(prefix_string("( A + B ) * C - ( D - E ) * ( F + G )"))





