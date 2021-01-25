def rob(nums: 'List[int]') -> int:
    """
    https://leetcode.com/problems/house-robber/
    Given a list of non-negative integers representing the amount of money of each house,
    determine the maximum amount of money you can rob tonight without alerting the police
    (the case when houses are adjacent).
    """
    if not len(nums): return 0
    if len(nums) == 1: return nums[0]

    d = [0]*len(nums)
    d[0], d[1] = nums[0], max(nums[0], nums[1])

    for i in range(2, len(nums)):
        d[i] = max(nums[i] + d[i-2], d[i-1])
    return d[-1]

if __name__ == '__main__':
    # equals 12: 2 + 9 + 1
    rob([2, 7, 9, 3, 1])