def strStr(haystack: str, needle: str) -> int:
    """
    https://leetcode.com/problems/implement-strstr/

    """
    if not needle: return 0
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1
