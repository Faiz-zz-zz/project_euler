"""

Starting in the top left corner of a 2×2 grid,
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?

"""
def naive():
    grid_size = 20
    total = [0]


    def dfs(i, j, total):
        print(i, j)
        if i == grid_size - 1 and j == grid_size - 1:
            total[0] += 1
        for move in [(1, 0), (0, 1)]:
            curr_i = i + move[0]
            curr_j = j + move[1]
            if 0 <= curr_i < grid_size and 0 <= curr_j < grid_size:
                dfs(curr_i, curr_j, total)

    dfs(0, 0, total)

    print(total)


def dynamic_programming():
    grid_size = 21
    grid = [[0 for i in range(grid_size)] for j in range(grid_size)]
    grid[0][0] = 1
    # set top row to 1
    # since there is only one way to reach any top row
    # set left row to 1 as well
    for i in range(grid_size):
        grid[0][i] = 1
        grid[i][0] = 1

    for i in range(1, grid_size):
        for j in range(1, grid_size):
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

    for row in grid:
        print(row)

dynamic_programming()
