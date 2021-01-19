def lengthOfLIS(nums: 'List[int]') -> int:
    """
    https://leetcode.com/problems/longest-increasing-subsequence/submissions/
    Given an integer array nums,
    return the length of the longest strictly increasing subsequence.
    """
    n = len(nums)
    ends_arr = [None] * (n)
    ends_arr[0] = 0
    length = 1
    prev = [None] * n

    for i in range(1, n):
        left, right = 0, length
        if nums[ends_arr[right - 1]] < nums[i]:
            j = right
        else:
            while right - left > 1:
                mid = (right + left) // 2
                if nums[ends_arr[mid - 1]] < nums[i]:
                    left = mid
                else:
                    right = mid
            j = left

        prev[i] = ends_arr[j - 1]
        if j == length or nums[i] < nums[ends_arr[j]]:
            ends_arr[j] = i
            length = max(length, j + 1)
    return length