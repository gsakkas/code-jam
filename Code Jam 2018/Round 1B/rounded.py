#!/usr/bin/env python


def read_int():
    return int(raw_input())


def read_many_ints():
    return map(int, raw_input().split())


def solve(n, langs):
    ls = read_many_ints()
    maxx = 0
    remaining = n - sum(ls)
    vals = map(lambda x: 100.0 * x / n, range(max(ls) + remaining + 1))
    rvals = map(lambda x: round(x), vals)
    sofar = sum(map(lambda x: rvals[x], ls))
    quant = rvals[1]
    maxx = sofar + quant * remaining
    for i in xrange(2, remaining + 1):
        if rvals[i] > vals[i]:
            newm = sofar + rvals[i] * (remaining / i) + \
                quant * (remaining % i)
            if newm > maxx:
                maxx = newm
                break
    needed = []
    for i, ll in enumerate(ls):
        if rvals[ll] < vals[ll]:
            for j in xrange(1, remaining + 1):
                if rvals[j + ll] > vals[j + ll]:
                    needed.append((j, i))
                    break
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
                for j in xrange(1, remaining + 1):
                    newm = sofar + rvals[j] * (remaining / j) + \
                        quant * (remaining % j)
                    if newm > maxx:
                        maxx = newm
                        break
        else:
            break
    return int(maxx)


if __name__ == "__main__":
    t = read_int()
    for test in xrange(1, t + 1):
        n, langs = read_many_ints()
        print "Case #{}: {}".format(test, solve(n, langs))
    exit(0)
