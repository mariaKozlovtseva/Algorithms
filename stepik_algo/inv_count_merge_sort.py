def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    global inv_count
    tmp_arr = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            tmp_arr.append(left[i])
            i += 1
        else:
            tmp_arr.append(right[j])
            inv_count += len(left) - i
            j += 1
    tmp_arr.extend(left[i:])
    tmp_arr.extend(right[j:])
    return tmp_arr

def main():
    _ = int(input())
    l = list((map(int, input().split())))
    merge_sort(l)
    print(inv_count)

if __name__ == '__main__':
    inv_count = 0
    main()