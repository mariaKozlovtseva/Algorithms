def threeSum(nums):
    """
    https://leetcode.com/problems/3sum/
    :param nums:
    :return:
    """
    res = []
    if not nums or len(nums) < 3:
        return res
    nums.sort()

    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1

        while l < r:
            curr_sum = nums[i] + nums[l] + nums[r]
            if curr_sum < 0:
                l += 1
            elif curr_sum > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                while l < len(nums)-1 and nums[l] == nums[l + 1]:
                    l += 1
                while r > 0 and r > l and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
    return res
