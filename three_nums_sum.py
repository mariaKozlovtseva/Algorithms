def three_number_sum(arr, sum):
    '''
    Computes list of sub-arrays of length 3 from initial array,
    where sum of each sub-array is equal to parameter "sum"
    :param arr: array
    :param sum: desired sum of array
    :return: array of tripplets
    '''
    arr.sort()
    result_arr = []
    for idx in range(len(arr)):
        left = idx + 1
        right = len(arr)-1
        while left < right:
            curr_sum = arr[idx] + arr[right] + arr[left]
            if curr_sum == sum:
                result_arr.append([arr[idx], arr[right], arr[left]])
                right -= 1
                left += 1
            if curr_sum < sum:
                left += 1
            if curr_sum > sum:
                right -= 1
    return  result_arr

if __name__ == '__main__':
    print(three_number_sum([12,3,1,2,-6,5,-8,6], 0))
