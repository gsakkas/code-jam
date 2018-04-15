from math import floor
from operator import itemgetter


def read_int():
    return int(raw_input())


def read_many_ints():
    return map(int, raw_input().split())


def find_quant(cashier, t):
    return max(0, min(cashier[0],
                      int(floor((t - cashier[2]) / cashier[1]))))


def solve(r, b, c):
    cashiers = [read_many_ints() for _ in xrange(c)]
    start = 1
    max_s = max(cashiers, key=itemgetter(1))[1]
    max_p = max(cashiers, key=itemgetter(2))[2]
    end = max_s * b + max_p
    while start <= end:
        t = start + (end - start) / 2
        quants = sorted(map(lambda x: find_quant(x, t), cashiers),
                        cmp=lambda x, y:
                        1 if x < y else 0 if x == y else -1)[:r]
        if b > reduce(lambda x, y: x + y, quants):
            start = t + 1
        else:
            end = t - 1
    return start


if __name__ == "__main__":
    t = read_int()
    for test in xrange(t):
        r, b, c = read_many_ints()
        print "Case #{}: {}".format(test + 1, solve(r, b, c))
    exit(0)
