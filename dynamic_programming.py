def fib(n, memoize={1:0, 2:1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = fib(n-1, memoize) + fib(n-2, memoize)
        return memoize[n]

def levenstein_dist(word_a, word_b):
    arr = [[i+j if i*j==0 else 0 for j in range(len(word_b)+1)]
           for i in range(len(word_a)+1)]
    for i in range(1, len(word_a)+1):
        for j in range(1, len(word_b)+1):
            if word_a[i-1] == word_b[j-1]:
                arr[i][j] = arr[i-1][j-1]
            else:
                arr[i][j] = 1 + min(arr[i-1][j-1],
                                    arr[i-1][j], arr[i][j-1])
    return arr[len(word_a)][len(word_b)]

def maxSubArray(nums: list) -> int:
    if len(nums) == 1:
        return nums[0]
    res_arr = [0]*len(nums)
    res_arr[0] = nums[0]
    for i in range(1,len(nums)):
        res_arr[i] = max(nums[i], nums[i] + res_arr[i-1])
    return max(res_arr)

if __name__ == '__main__':
    print(fib(10))
    print(levenstein_dist('me', 'mike'))
    print(maxSubArray([-2,1,-3,4,-1,2,-5,6]))