from math import floor, ceil


def read_int():
    return int(raw_input())


def read_many_ints():
    return map(int, raw_input().split())


def read_cake(r, c):
    return [raw_input() for _ in xrange(r)]


def solve(n, p):
    rs = read_many_ints()
    qs = [read_many_ints() for _ in xrange(n)]
    servs = []
    for i, q in enumerate(qs):
        servings = map(lambda x: range(int(ceil(x / (1.1 * rs[i]))),
                                       int(floor(x / (0.9 * rs[i]))) + 1), q)
        servings = filter(None, servings)
        servings = sorted(servings, key=lambda x: x[0])
        servings = sorted(servings, key=lambda x: x[-1])
        servings = map(set, servings)
        servs.append(servings)

    # print servs
    # results = 0
    # for serv in servs[0]:
    #     sol = []
    #     flag = False
    #     for q in servs[1:]:
    #         similar = filter(lambda x: serv & x, q)
    #         if similar:
    #             sol.append(similar[0])
    #         else:
    #             flag = True
    #             break
    #     if flag:
    #         continue
    #     for i, s in enumerate(sol):
    #         servs[i + 1].remove(s)
    #     results += 1
    # return results
    results = 0
    while reduce(lambda x, y: x and y, map(lambda x: x != [], servs)):
        if reduce(lambda x, y: x & y[0], servs, servs[0][0]):
            for i in xrange(n):
                servs[i].pop(0)
            results += 1
        else:
            upper = servs[0][-1]
            idx = 0
            for i in xrange(1, n):
                if upper > servs[i][0]:
                    upper = servs[i][0]
                    idx = i
            servs[idx].pop(0)
    return results


if __name__ == "__main__":
    t = read_int()
    for test in xrange(1, t + 1):
        n, p = read_many_ints()
        print "Case #{}: {}".format(test, solve(n, p))
    exit(0)
