def monotonic(arr, if_true_false=False):
    """
    Check whether array is monotonic or not
    :param arr: array of different numbers
    :return: string "Monotonic" / "Not monotonic" or if  True / False
    """
    decreasing = False
    increasing = False
    idx = 0
    while not increasing and idx < len(arr)-1:
        # use abs() as we may have negative values
        if abs(arr[idx]) >  abs(arr[idx+1]):
            increasing = True
        else:
            decreasing = True
        idx += 1
    if if_true_false:
        return True if (decreasing and not increasing) else False
    return "Monotonic" if (decreasing and not increasing) else "Not monotonic"


if __name__ == '__main__':
    print(monotonic([-2,-4,-10,-100]))
    print(monotonic([0,-1,-2,1,4], if_true_false=True))