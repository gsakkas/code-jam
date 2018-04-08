import sys


def read_int():
    return int(raw_input())


def read_two():
    return map(int, raw_input().split())


def find_rectangle(a):
    if a < 100:
        return (4, 5)
    else:
        return (14, 15)


def select_cell(score_grid):
    return min([(min(row), (i, row.index(min(row))))
                for i, row in enumerate(score_grid)])


def update_scores(score_grid, x, y, maxx, maxy):
    indices = [(x, y), (x + 1, y + 1), (x + 1, y), (x, y + 1), (x - 1, y - 1),
               (x - 1, y), (x, y - 1), (x + 1, y - 1), (x - 1, y + 1)]
    indices = filter(lambda x: -1 < x[0] < maxx and -1 < x[1] < maxy, indices)
    for i, j in indices:
        score_grid[i][j] += 1
    return score_grid


def solve(a):
    position = 2
    dimx, dimy = find_rectangle(a)
    grid = [[True for _ in xrange(dimy)] for _ in xrange(dimx)]
    score_grid = [[0 for _ in xrange(dimy)] for _ in xrange(dimx)]
    for i in xrange(dimx):
        score_grid[i][0] = 10000
        score_grid[i][-1] = 10000
    for j in xrange(dimy):
        score_grid[0][j] = 10000
        score_grid[-1][j] = 10000

    while True:
        i, j = select_cell(score_grid)[1]
        print i + position, j + position
        sys.stdout.flush()
        x, y = read_two()
        if x < 1 and y < 1:
            break
        x -= position
        y -= position
        if grid[x][y]:
            grid[x][y] = False
            score_grid = update_scores(score_grid, x, y, dimx, dimy)


if __name__ == "__main__":
    t = read_int()
    for test in xrange(t):
        a = read_int()
        solve(a)
    exit(0)
