# различные слагаемые
# математический подход
def extend_num(n):
    res = []
    i = 1
    while n > 2*i:
        n -= i
        res.append(i)
        i += 1
    else:
        res.append(n)
    print(str(len(res)) +'\n' + ' '.join(map(str,res)))

def extend_num2(n):
    res = []
    for i in range(1, n+1):
        if n-i >= i+1:
            res.append(i)
            n -= i
        else:
            res.append(n)
            break
    print(str(len(res)) + '\n' + ' '.join(map(str, res)))

if __name__ == '__main__':
    n = int(input())
    extend_num2(n)
