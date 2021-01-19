def find_largest_nonincr_subseq(arr, n):
    # ends_arr keeps the smallest value to build a subseq
    # where i (index of arr) = j (index of ends_arr)
    ends_arr = [None]*(n)
    # base case: when 1st element is considered to be the longest noninc subseq
    ends_arr[0] = 0
    length = 1
    # prev[i] = ends_arr[j-1] is a previous value
    # where i - index of arr
    prev = [None]*n

    for i in range(1, n):
        left, right = 0, length
        if arr[ends_arr[right-1]] >= arr[i]:
            j = right
        else:
            while right - left > 1:
                mid = (right + left) // 2
                if arr[ends_arr[mid-1]] >= arr[i]:
                    left = mid
                else:
                    right = mid
            j = left
        prev[i] = ends_arr[j-1]
        if j == length or arr[i] > arr[ends_arr[j]]:
            ends_arr[j] = i
            length = max(length, j+1)

    print(length, end='\n')
    pos = ends_arr[length-1]
    res = []
    for _ in range(length):
        res.append(pos+1)
        pos = prev[pos]
    print(' '.join(map(str, reversed(res))))

def main():
    n = int(input())
    arr = list(map(str, input().split()))
    find_largest_nonincr_subseq(arr, n)

if __name__ == '__main__':
    main()