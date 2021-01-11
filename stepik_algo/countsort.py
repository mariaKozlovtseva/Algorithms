# сортировка подсчётом

def countsort(arr):
    m = [0]*11
    for i in range(len(arr)):
        m[arr[i]] += 1
    for j in range(2, len(m)):
        m[j] += m[j-1]
    res = [0]*len(arr)
    for i in range(len(arr)-1, -1, -1):
        res[m[arr[i]]-1] = arr[i]
        m[arr[i]] -= 1
    print(' '.join(map(str, res)))

def main():
    _ = int(input())
    l = [int(i) for i in input().split(' ')]
    countsort(l)

if __name__ == '__main__':
    main()