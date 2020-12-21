def maxArea(height) -> int:
    """
    https://leetcode.com/problems/container-with-most-water/
    :param A: list of integers (peaks)
    :return: max area between any two elements of a list
    """
    left, right = 0, len(height) - 1
    area = 0
    while left < right:
        area = max(area, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return area