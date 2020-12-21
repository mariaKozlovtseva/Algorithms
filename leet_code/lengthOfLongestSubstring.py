def lengthOfLongestSubstring(s: str):
    """
    https://leetcode.com/problems/longest-substring-without-repeating-characters/

    """
    if not s: return 0
    result, start = 0, 0
    mp = {}
    for i in range(len(s)):
        if s[i] in mp:
            start = max(start, mp[s[i]] + 1)
        mp[s[i]] = i
        result = max(result, i - start + 1)
    return result