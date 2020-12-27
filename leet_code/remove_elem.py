def removeElement(nums, val: int) -> int:
    """
    https://leetcode.com/problems/remove-element/
    :param nums: a list of integers which should be modified
    :param val: value to remove
    :return: length of the given list without elements with value == val
    """
    i = 0
    for right in range(1,len(nums)):
        if nums[right] != val:
            nums[i] = nums[right]
            i += 1
    return i

def moveZeroes(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    Similar tp the previous task.
    https://leetcode.com/problems/move-zeroes/
    """
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1