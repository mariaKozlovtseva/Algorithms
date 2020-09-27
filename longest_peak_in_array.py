def longest_peak(arr):
    length = 0
    i = 1
    while i < len(arr) - 1:
        isPeak = arr[i] > arr[i-1] and arr[i] > arr[i+1]
        if not isPeak:
            i += 1
            continue
        leftIdx = i-2
        while leftIdx > 0 and arr[leftIdx] < arr[leftIdx+1]:
            leftIdx -= 1
        rightIdx = i + 2
        while rightIdx < len(arr) and arr[rightIdx] < arr[rightIdx-1]:
            rightIdx += 1
        current_length = rightIdx - leftIdx - 1
        length = max(current_length, length)
        i = rightIdx
    return length

if __name__ == '__main__':
    arr = [1,2,3,3,4,0,10,6,-3,-4]
    print(longest_peak(arr))
