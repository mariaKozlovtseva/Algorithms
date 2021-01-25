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

def backpack(max_weight, n_items, weights, prices):
    arr = [[0 for j in range(max_weight + 1)] for i in range(n_items + 1)]
    for i in range(1, n_items + 1):
        for j in range(1, max_weight + 1):
            arr[i][j] = arr[i - 1][j]
            if weights[i - 1] <= j:
                v = arr[i - 1][j - weights[i - 1]] + prices[i - 1]
                arr[i][j] = max(arr[i][j], v)
    return arr[-1][-1]

def min_coin_change(change, coins):
    d = [float('inf')]*(change+1)
    d[0] = 0
    for i in range(change+1):
        for c in coins:
            if i >= c:
                d[i] = min(d[i], 1 + d[i-c])
        # print(d)
    print(d[change])

def ladder(n: 'length of array', arr):
    """
    Given number 1<= n <=10^2 stairs of ladder and array of integers that mark the steps.
    Find the maximum amount you can get by going up the stairs
    (from the zero to the n-th rung), going up one or two rungs each time.

    """
    if n < 2:
        print(arr[0])
        return
    prev, next = 0, arr[0]
    for i in range(1, n):
        prev, next = next, max(prev, next) + arr[i]
    print(next)


if __name__ == '__main__':
    print(fib(10))
    print(levenstein_dist('me', 'mike'))
    print(maxSubArray([-2,1,-3,4,-1,2,-5,6]))
    items = 4
    weights = [0, 1, 4, 5]
    prices = [15, 20, 30, 35]
    print(backpack(6, items, weights, prices))
    min_coin_change(15, [1, 2, 5, 10])