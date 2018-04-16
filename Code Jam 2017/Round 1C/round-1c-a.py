from math import pi


def read_int():
    return int(raw_input())


def read_many_ints():
    return map(int, raw_input().split())


def read_many(n, k):
    return [read_many_ints() for _ in xrange(n)]


def solve(n, k):
    pancakes = read_many(n, k)
    pancakes.sort(key=lambda x: x[0] * x[1], reverse=True)
    pans = pancakes[:k]
    rest = pancakes[k:]
    pancakes.sort(key=lambda x: x[0] * x[0] + 2 * x[0] * x[1], reverse=True)
    max_area = -1.0
    for big in pancakes:
        if big in rest:
            pp = big
            result = pi * pp[0] * pp[0] + 2 * pi * pp[0] * pp[1]
            for p in pans[:-1]:
                result += 2 * pi * p[0] * p[1]
            if result > max_area:
                max_area = result
        else:
            pp = max(pans, key=lambda x: x[0])
            result = pi * pp[0] * pp[0]
            for p in pans:
                result += 2 * pi * p[0] * p[1]
            if result > max_area:
                max_area = result
    return max_area


if __name__ == "__main__":
    t = read_int()
    for test in xrange(1, t + 1):
        n, k = read_many_ints()
        print "Case #{}: {}".format(test, solve(n, k))
    exit(0)
