def read_int():
    return int(raw_input())


def read_many_ints():
    return map(int, raw_input().split())


def solve(n):
    ws = read_many_ints()
    large = 10 ** 100
    sums = [[large] * min(139, n) for _ in xrange(n)]
    for i in xrange(n):
        sums[i][0] = ws[i]
    # sums = {}
    # sums[0] = ws[0]
    # for i in xrange(1, n):
    #     sums[i] = 0

    for i in xrange(1, n):
        for j in xrange(1, min(139, i + 1)):
            if sums[i - 1][j - 1] <= 6 * ws[i]:
                sums[i][j] = min(sums[i - 1][j - 1] + ws[i], sums[i - 1][j])
            else:
                sums[i][j] = sums[i - 1][j]
    j = n - 1
    while j >= 0 and sums[n - 1][j] == large:
        j -= 1
    return j + 1


if __name__ == "__main__":
    t = read_int()
    for test in xrange(1, t + 1):
        n = read_int()
        print "Case #{}: {}".format(test, solve(n))
    exit(0)
