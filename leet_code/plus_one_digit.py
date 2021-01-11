def plusOne(digits):
    """
    https://leetcode.com/problems/plus-one/

    """
    j = len(digits)-1
    while j != -1:
        if digits[j] == 9:
            digits[j] = 0
            j -= 1
        else:
            digits[j] += 1
            return digits
    return [1] + digits

def plusOne_2(digits):
    # this operation won't be done
    # and the task description also said there is no leading 0s
    # but some of tests was [0, 0]
    if sum(set(digits)) == 0:
        digits[-1] = 1
        return digits
    num = int(''.join(map(str, digits))) + 1
    num = str(num)
    ans = []
    for i in num:
        ans.append(int(i))
    return ans

# with a large number containing only 9s
digits = [9]*len(range(100000))

from time import perf_counter
start = perf_counter()
plusOne(digits)
# 0.036
print('end: {}'.format(str(perf_counter() - start)))

start = perf_counter()
plusOne_2(digits)
# 0.003 - 10 times faster
print('end: {}'.format(str(perf_counter() - start)))

# with a number without all 9s
digits = list(range(10000, 1, -1))
start = perf_counter()
plusOne(digits)
# 0.00006 - 1000 times faster
print('end: {}'.format(str(perf_counter() - start)))

start = perf_counter()
plusOne_2(digits)
# 0.06
print('end: {}'.format(str(perf_counter() - start)))