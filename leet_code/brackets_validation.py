def isValid(s: str) -> bool:
    """
    https://leetcode.com/problems/valid-parentheses/

    """
    reverse_br = {'}':'{',
                  ')':'(',
                  ']':'['}
    stack = []
    for i in range(len(s)):
        if s[i] in reverse_br and stack:
            if reverse_br[s[i]] == stack[-1]:
                stack.pop()
            else: break
        else:
            stack.append(s[i])
    return not stack

