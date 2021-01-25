def minPathSum(grid: 'List[List[int]]') -> int:
    """
    https://leetcode.com/problems/minimum-path-sum/
    :param grid:
    :return:
    """
    row, col = len(grid), len(grid[0])
    d = [[0 for j in range(col)] for i in range(row)]
    d[0][0] = grid[0][0]

    # initialize 1st row
    for j in range(1, col):
        d[0][j] = d[0][j-1] + grid[0][j]
    # initialize 1st column
    for i in range(1, row):
        d[i][0] = d[i-1][0] + grid[i][0]

    # for each other cell choose min from top and left neighbour
    for i in range(1, row):
        for j in range(1, col):
            d[i][j] = min(d[i-1][j],
                          d[i][j-1]) + grid[i][j]
    return d[row-1][col-1]

if __name__ == '__main__':
    # equal 7
    print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))