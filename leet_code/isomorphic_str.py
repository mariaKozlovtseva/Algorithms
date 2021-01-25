def isIsomorphic(s: str, t: str) -> bool:
    """
    https://leetcode.com/problems/isomorphic-strings/
    """
    d = {}
    for i in range(len(s)):
        if s[i] not in d and t[i] not in d.values():
            d[s[i]] = t[i]
        elif s[i] in d and d[s[i]] == t[i]:
            continue
        else:
            return False
    return True

if __name__ == '__main__':
    print(isIsomorphic("badc", "babd"))
    print(isIsomorphic("add", "egg"))