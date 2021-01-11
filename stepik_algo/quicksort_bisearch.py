def partition(arr):
    pivot = (arr[0] + arr[len(arr)//2] + arr[-1]) // 3
    ls, gr, eq = [], [], []
    for x in arr:
        if x > pivot: gr.append(x)
        elif x < pivot: ls.append(x)
        else: eq.append(x)
    return ls, eq, gr

def quicksort(arr):
    while len(arr) > 1:
        ls, eq, gr = partition(arr)
        if len(ls) < len(gr):
            ls = quicksort(ls)
            return ls + eq + quicksort(gr)
        elif len(ls) > len(gr):
            gr = quicksort(gr)
            return quicksort(ls) + eq + gr
        else:
            return quicksort(ls) + eq + quicksort(gr)
    return arr

def bi_search(arr, point, i):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + (r-l) // 2
        if arr[mid] <= point - i:
            l = mid + 1
        elif arr[mid] > point - i:
            r = mid - 1
    return l

def main():
    n, m = tuple(map(int,input().split()))
    left, right = [], []
    for _ in range(n):
        l_r_point = tuple(map(int,input().split()))
        left.append(l_r_point[0])
        right.append(l_r_point[1])
    points = tuple(map(int, input().split()))
    left, right = quicksort(left), quicksort(right)
    for p in points:
        print(bi_search(left, p, 0) - bi_search(right, p, 1), end=' ')


if __name__ == '__main__':
    main()