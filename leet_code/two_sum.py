def twoSum(nums, target):
    """
    https://leetcode.com/problems/two-sum/

    """
    d = dict()
    for i in range(len(nums)):
        if nums[i] not in d:
            residual = target - nums[i]
            d[residual] = i
        else:
            return [d[nums[i]], i]