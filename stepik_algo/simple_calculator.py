def simple_calculator(n):
    opers = [lambda x: 3*x, lambda x: 2*x, lambda x: x+1]
    d = list(range(n))
    # will be used in the end to make a sequence of calculated values to reach n
    prev = dict(zip(list(range(1, 6)), d))

    for i in range(1, n):
        for oper in opers:
            v = oper(i)
            if v <= n and 1 + d[i-1] < d[v-1]:
                d[v-1] = 1 + d[i-1]
                prev[v] = i

    res = [n]
    for _ in range(d[n-1]):
        res.append(prev[res[-1]])
    print(d[n - 1])
    print(*list(reversed(res)))

if __name__ == '__main__':
    n = int(input())
    simple_calculator(n)