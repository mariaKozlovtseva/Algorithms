def move_elem_to_end(arr, value):
    '''
    Moves elements of array to end
    with value equal = parameter value
    :return: shifted array
    '''
    if value not in set(arr):
        raise ValueError("Array must contain at least one element with such value")
    # variables to track position in array
    head = 0
    tail = -1
    while (head + -tail) < len(arr):
        if arr[head] == value:
            arr[tail], arr[head] = value, arr[tail]
            tail -= 1
        else:
            head += 1
    return arr

if __name__ == '__main__':
    print(move_elem_to_end([2, 1, 2, 2, 4, 3, 2], 2))