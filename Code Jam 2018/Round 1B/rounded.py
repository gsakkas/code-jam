#!/usr/bin/env python


def read_int():
    return int(raw_input())


def read_many_ints():
    return map(int, raw_input().split())


def solve(n, langs):
    ls = read_many_ints()
    remaining = n - sum(ls)
    vals = map(lambda x: 100.0 * x / n, range(max(ls) + remaining + 1))
    rvals = map(lambda x: round(x), vals)
    nextr = []
    nn = len(rvals)
    for i in xrange(len(rvals) - 1, -1, -1):
        if rvals[i] > vals[i]:
            nn = i
        nextr.insert(0, nn)
    sofar = reduce(lambda x, y: x + rvals[y], ls, 0)
    quant = rvals[1]
    maxx = sofar + quant * remaining
    i = 1
    while i <= remaining and rvals[i] <= vals[i]:
        i += 1
    mx_quant = rvals[i]
    mx_i = i
    newm = sofar + mx_quant * (remaining / mx_i) + quant * (remaining % mx_i)
    if newm > maxx:
        maxx = newm

    temp = filter(lambda x: rvals[x[1]] < vals[x[1]], enumerate(ls))
    temp = map(lambda x: (nextr[x[1]] - x[1], x[0]), temp)
    needed = filter(lambda x: x[0] <= remaining, temp)
    needed.sort(key=lambda x: x[0])
    for need, i in needed:
        if remaining - need >= 0:
            remaining -= need
            sofar -= rvals[ls[i]]
            sofar += rvals[ls[i] + need]
            if remaining == 0:
                if sofar > maxx:
                    maxx = sofar
            else:
                newm = sofar + mx_quant * (remaining / mx_i) + \
                    quant * (remaining % mx_i)
                if newm > maxx:
                    maxx = newm
        else:
            break
    return int(maxx)


if __name__ == "__main__":
    t = read_int()
    for test in xrange(1, t + 1):
        n, langs = read_many_ints()
        print "Case #{}: {}".format(test, solve(n, langs))
    exit(0)
