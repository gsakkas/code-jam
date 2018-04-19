def read_int():
    return int(raw_input())


def read_many_ints():
    return map(int, raw_input().split())


def read_many(n):
    return [read_many_ints() for _ in xrange(n)]


def column(matrix, i):
    return [row[i] for row in matrix]


def solve(n):
    lists = reduce(lambda x, y: x + y, read_many(2 * n - 1))
    lists.sort()
    result = filter(lambda x: len(
        filter(lambda y: y == x, lists)) % 2 == 1, lists)
    result = sorted(list(set(result)))
    return ' '.join(map(str, result))


if __name__ == "__main__":
    t = read_int()
    for test in xrange(1, t + 1):
        n = read_int()
        print "Case #{}: {}".format(test, solve(n))
    exit(0)
