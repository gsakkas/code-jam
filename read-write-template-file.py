#!/usr/bin/env python


def read_int():
    return int(raw_input())


def read_many_ints():
    return map(int, raw_input().split())


def read_many(r, c):
    return [read_many_ints() for _ in xrange(r)]


def solve(r, c):
    int_2d_array = read_many(r, c)
    pass


if __name__ == "__main__":
    t = read_int()
    for test in xrange(1, t + 1):
        rows, columns = read_many_ints()
        print "Case #{}: {}".format(test, solve(rows, columns))
    exit(0)
