def read_int():
    return int(raw_input())


def read_many_ints():
    return map(int, raw_input().split())


def read_map(r, c):
    return [map(lambda x: False if x == '.' else True, raw_input())
            for _ in xrange(r)]


def solve(r, c, h, v):
    grid = read_map(r, c)

    chips = 0
    row_sums = []
    for i in xrange(r):
        temp = len(filter(None, grid[i]))
        chips += temp
        row_sums.append(chips)

    chips = 0
    col_sums = []
    for j in xrange(c):
        temp = len(filter(None, map(lambda x: x[j], grid)))
        chips += temp
        col_sums.append(chips)
    if chips % ((h + 1) * (v + 1)) > 0:
        return "IMPOSSIBLE"
    else:
        must_have = chips / ((h + 1) * (v + 1))
        row_must_have = chips / (h + 1)
        col_must_have = chips / (v + 1)

        row_intervals = []
        interval_so_far = []
        needed = row_must_have
        for i, val in enumerate(row_sums):
            interval_so_far.append(i)
            if needed == val:
                row_intervals.append(interval_so_far)
                interval_so_far = []
                needed += row_must_have
        if interval_so_far != []:
            return "IMPOSSIBLE"

        col_intervals = []
        interval_so_far = []
        needed = col_must_have
        for i, val in enumerate(col_sums):
            interval_so_far.append(i)
            if needed == val:
                col_intervals.append(interval_so_far)
                interval_so_far = []
                needed += col_must_have
        if interval_so_far != []:
            return "IMPOSSIBLE"

        for row in row_intervals:
            for col in col_intervals:
                chips = 0
                for i in row:
                    for j in col:
                        chips += grid[i][j]
                if chips != must_have:
                    return "IMPOSSIBLE"
        return "POSSIBLE"


if __name__ == "__main__":
    t = read_int()
    for test in xrange(t):
        r, c, h, v = read_many_ints()
        print "Case #{}: {}".format(test + 1, solve(r, c, h, v))
    exit(0)
