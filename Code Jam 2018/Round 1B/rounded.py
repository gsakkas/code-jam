#!/usr/bin/env python


def read_int():
    return int(raw_input())


def read_many_ints():
    return map(int, raw_input().split())


def remainder(x):
    return x - int(x)


def solve(n, langs):
    ls = read_many_ints()

    quant = 100.0 / n
    rquant = round(quant)
    if remainder(quant) == 0:
        return 100

    sofar = sum([round(100.0 * x / n) for x in ls])
    remaining = n - sum(ls)
    if remainder(quant) >= 0.5:
        return int(sofar + rquant * remaining)

    nextr = []
    nn = max(ls) + remaining + 1
    lenn = nn - 1
    for i in xrange(lenn, -1, -1):
        if remainder(100.0 * i / n) >= 0.5:
            nn = i
        nextr.insert(0, nn)

    maxx = sofar + rquant * remaining
    i = 1
    while i <= remaining and remainder(100.0 * i / n) < 0.5:
        i += 1
    mx_quant = round(100.0 * i / n)
    mx_i = i
    newm = sofar + mx_quant * (remaining / mx_i) + rquant * (remaining % mx_i)
    if newm > maxx:
        maxx = newm

    ls.sort(key=lambda x: remainder(100.0 * x / n), reverse=True)
    for l in ls:
        need = nextr[l] - l
        if remaining - need >= 0:
            remaining -= need
            sofar += round(100.0 * nextr[l] / n) - round(100.0 * l / n)
            if remaining == 0:
                if sofar > maxx:
                    maxx = sofar
            else:
                newm = sofar + mx_quant * (remaining / mx_i) + \
                    rquant * (remaining % mx_i)
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
