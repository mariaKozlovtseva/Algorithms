def backpack(max_weight, n_items, weights):
    # items without prices
    arr = [[0 for j in range(max_weight + 1)] for i in range(n_items + 1)]
    for i in range(1, n_items + 1):
        for j in range(1, max_weight + 1):
            arr[i][j] = arr[i-1][j]

            if weights[i - 1] <= j:
                v = arr[i - 1][j - weights[i - 1]] + weights[i - 1]
                arr[i][j] = max(arr[i][j], v)
    return arr[-1][-1]


if __name__ == '__main__':
    capacity, n = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    print(backpack(capacity, n, weights))