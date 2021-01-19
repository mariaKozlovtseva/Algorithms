def find_largest_subseq(arr):
    d = [1]*len(arr)
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[j] <= arr[i] and not arr[i] % arr[j] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
    return max(d)

def main():
    _ = int(input())
    arr = list(map(int, input().split()))
    find_largest_subseq(arr)

if __name__ == '__main__':
    main()