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

def eval_postfix(postfix_s):
    postfix_s = postfix_s.split()
    stack = Stack()
    for elem in postfix_s:
        if elem in "0123456789":
            stack.push(int(elem))
        else:
            oper2 = stack.pop()
            oper1 = stack.pop()
            result = calculate(elem, oper1, oper2)
            stack.push(result)
    return stack.pop()

def calculate(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

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

def eval_prefix(prefix_s):
    prefix_s = prefix_s.split()
    stack = Stack()
    for elem in prefix_s[::-1]:
        if elem in "0123456789":
            stack.push(int(elem))
        else:
            oper1 = stack.pop()
            oper2 = stack.pop()
            result = calculate(elem, oper1, oper2)
            stack.push(result)
    return stack.pop()

if __name__ == '__main__':
    print(postfix_string("( A + B ) * C - ( D - E ) * ( F + G )"))
    print(prefix_string("( A + B ) * C - ( D - E ) * ( F + G )"))
    print(eval_postfix('7 8 + 3 2 + /'))
    print(eval_prefix('+ 5 * 4 3'))





