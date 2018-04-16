from math import floor, ceil
from itertools import permutations


def read_int():
    return int(raw_input())


def read_many_ints():
    return map(int, raw_input().split())


def read_cake(r, c):
    return [raw_input() for _ in xrange(r)]


def intersect(bounds1, bounds2):
    if bounds1 == [] or bounds2 == []:
        return []
    if bounds1[0] == bounds2[0]:
        return [bounds1[0], min(bounds1[1], bounds2[1])]
    elif bounds1[0] < bounds2[0]:
        if bounds2[0] <= bounds1[1]:
            return [bounds2[0], bounds1[1]]
        else:
            return []
    elif bounds2[0] < bounds1[0]:
        if bounds1[0] <= bounds2[1]:
            return [bounds1[0], bounds2[1]]
        else:
            return []


def solve(n, p):
    rs = read_many_ints()
    qs = [read_many_ints() for _ in xrange(n)]
    servs = []
    for i, q in enumerate(qs):
        servings = map(lambda x:
                       [int(ceil(x * 10.0 / (11 * rs[i]))),
                        int(floor(x * 10.0 / (9 * rs[i])))], q)
        servings = filter(lambda x: x[0] <= x[1], servings)
        servings = sorted(servings, key=lambda x: x[-1])
        servings = sorted(servings, key=lambda x: x[0])
        servs.append(servings)

    # Solution for small testcase
    if n == 1:
        return len(servs[0])
    elif n == 2 and p <= 8:
        list1 = []
        list2 = []
        if len(servs[0]) >= len(servs[1]):
            list1 = servs[0]
            list2 = servs[1]
        else:
            list1 = servs[1]
            list2 = servs[0]
        perms = [zip(x, list2) for x in permutations(list1, len(list2))]
        return max(map(lambda x:
                       len(filter(None, map(lambda x:
                                            intersect(x[0], x[1]), x))),
                       perms))
    # Solution for large testcase, works for small also
    else:
        results = 0
        while reduce(lambda x, y: x and y, map(lambda x: x != [], servs)):
            if reduce(lambda x, y: intersect(x, y[0]), servs, servs[0][0]):
                for i in xrange(n):
                    servs[i].pop(0)
                results += 1
            else:
                upper = servs[0][-1]
                idx = 0
                for i in xrange(1, n):
                    if upper > servs[i][-1]:
                        upper = servs[i][-1]
                        idx = i
                servs[idx].pop(0)
        return results


if __name__ == "__main__":
    t = read_int()
    for test in xrange(1, t + 1):
        n, p = read_many_ints()
        print "Case #{}: {}".format(test, solve(n, p))
    exit(0)
