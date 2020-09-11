def smallest_difference(array1, array2):
    '''
    Given two arrays of different lengths find sub-arrays
    of two elements with minimal absolute difference
    '''
    array1.sort()
    array2.sort()
    idx1 = 0
    idx2 = 0
    smallest = float("inf")
    current = float("inf")
    smallest_pair = []

    while idx1 < len(array1) and idx2 < len(array2):
        first_num = array1[idx1]
        second_num = array2[idx2]
        current = abs(first_num - second_num)
        if first_num < second_num:
            idx1 += 1
        elif first_num > second_num:
            idx2 += 1
        else: # nums are equal
            smallest_pair = check_arr(smallest_pair, [first_num, second_num], current)
            idx1 += 1
            idx2 += 1
            smallest = 0
            continue
        if smallest >= current:
            smallest = current
            smallest_pair = check_arr(smallest_pair, [first_num, second_num], current)

    return smallest_pair, 'smallest absolute difference: ' + str(smallest)

def check_arr(smallest_pair, new_pair, current_diff):
    if smallest_pair: # exists
        # check
        if abs(smallest_pair[0][0] - smallest_pair[0][1]) > current_diff:
            smallest_pair = [new_pair]
        # if the same absolute difference - just expand array
        else:
            smallest_pair.append(new_pair)
        return  smallest_pair
    return [new_pair]


if __name__ == '__main__':
    print(smallest_difference([2,20,0,1,34,-8],[10,3,-1,6,-3]))