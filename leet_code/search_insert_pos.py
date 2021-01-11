def searchInsert(nums, target: int) -> int:
    """
    https://leetcode.com/problems/search-insert-position/

    """
    if target > nums[-1]:
        return len(nums)
    for i in range(len(nums)):
        if nums[i] - target >= 0:
            return i
    return 0


def searchInsert2(nums, target: int) -> int:
    left, right = 0, len(nums)-1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid -1
    if nums[right] < target:
        return right + 1
    elif nums[left] >= target:
        return left

from time import time
start = time()
searchInsert(list(range(1000000)), 999999)
# 0.205
print('end: {}'.format(str(time()-start)))
start = time()
searchInsert2(list(range(1000000)), 999999)
# 0.029 - almost 7 times faster
print('end: {}'.format(str(time()-start)))