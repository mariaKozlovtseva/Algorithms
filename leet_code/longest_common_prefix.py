def longestCommonPrefix(strs: list) -> str:
    """
    https://leetcode.com/problems/longest-common-prefix/

    """
    if not strs: return ''
    length  = min([len(i) for i in strs])
    res = strs[0][:length]
    i = 0
    while i < len(strs)-1:
        for j in range(length):
            if strs[i][j] != strs[i+1][j]:
                res = res[:j]
                break
        i += 1
    return res