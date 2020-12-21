def romanToInt(self, s: str) -> int:
    """
    https://leetcode.com/problems/roman-to-integer/

    """
    romans = dict(zip(('I', 'V', 'X', 'L', 'C', 'D', 'M', 'IV', 'IX', 'XL', 'XC', 'CD', 'CM'),
                      (1, 5, 10, 50, 100, 500, 1000, 4, 9, 40, 90, 400, 900)))
    result, i = 0, 0
    while i < len(s):
        if s[i:i + 2] in romans:
            result += romans[s[i:i + 2]]
            i += 2
        else:
            result += romans[s[i]]
            i += 1
    return result


def intToRoman(number):
    """
    https://leetcode.com/problems/integer-to-roman/

    """
    nums = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    romans = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    result = ''
    if number < nums[len(nums) // 2]:
        i = len(nums) // 2
    else:
        i = len(nums)-1
    while number:
        div, number = divmod(number, nums[i])
        if div:
            if div > 1:
                result += div * romans[i]
            else:
                result += romans[i]
        i -= 1
    return result

