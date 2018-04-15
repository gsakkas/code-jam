def read_int():
    return int(raw_input())


def read_many_ints():
    return map(int, raw_input().split())


def read_cake(r, c):
    return [raw_input() for _ in xrange(r)]


def solve(r, c):
    cake = read_cake(r, c)
    if reduce(lambda x, y: x and y, map(lambda x: '?' not in x, cake)):
        return cake
    else:
        groups = {}
        captured = []
        for i in xrange(r):
            for j in xrange(c):
                if not cake[i][j] is '?':
                    groups[cake[i][j]] = [(i, j)]
                    captured.append((i, j))
        for i in xrange(r):
            first = True
            for j in xrange(c):
                if not cake[i][j] is '?':
                    if first:
                        cake[i] = cake[i][j] * j + cake[i][j:]
                        first = False
                    for y in xrange(j + 1, c):
                        if cake[i][y] is '?':
                            cake[i] = cake[i][:y] + \
                                cake[i][j] + cake[i][(y + 1):]
                        else:
                            j = y
                            break
            if first and i > 0:
                cake[i] = cake[i - 1]
        i = 0
        while cake[i][0] is '?':
            i += 1
        for j in xrange(i):
            cake[j] = cake[i]
        return cake


if __name__ == "__main__":
    t = read_int()
    for test in xrange(1, t + 1):
        r, c = read_many_ints()
        print "Case #{}:\n{}".format(test, '\n'.join(solve(r, c)))
    exit(0)
