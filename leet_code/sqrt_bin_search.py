def mySqrt(x: int) -> int:
    """
    https://leetcode.com/problems/sqrtx/
    Implementation of sqrt func using binary search
    """
    l, r = 0, x
    while l <= r:
        mid = (l + r) // 2
        if mid**2 <= x < (mid+1)**2:
            return mid
        elif mid**2 < x:
            l = mid + 1
        else:
            r = mid - 1

