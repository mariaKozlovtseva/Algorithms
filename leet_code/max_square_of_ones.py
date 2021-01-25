def maximalSquare(matrix: 'List[List[str]]') -> int:
    """
    https://leetcode.com/problems/maximal-square/
    Given an m x n binary matrix filled with 0's and 1's,
    find the largest square containing only 1's and return its area.
    """
    i, j = len(matrix), len(matrix[0])
    d = [[0 for _ in range(j+1)] for _ in range(i+1)]
    max_side = 0
    for m in range(1, i+1):
        for n in range(1, j+1):
            if matrix[m-1][n-1] != '0':
                d[m][n] = min(d[m-1][n],
                              d[m][n-1],
                              d[m-1][n-1]) + 1
                max_side = max(max_side, d[m][n])
    return max_side ** 2

