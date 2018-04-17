def read_int():
    return int(raw_input())


def read_many_ints():
    return map(int, raw_input().split())


def read_many(a):
    return [read_many_ints() for _ in xrange(a)]


def solve(ac, aj):
    cds = sorted(read_many(ac))
    cds = map(lambda x: x + [1], cds)
    for i in xrange(1, ac):
        if cds[i][0] == cds[i - 1][1]:
            cds[i - 1][1] = cds[i][1]
            cds[i][2] = 0
    cds = filter(lambda x: x[2] > 0, cds)
    ctime = reduce(lambda x, y: x - y[1] + y[0], cds, 720)
    jks = sorted(read_many(aj))
    jks = map(lambda x: x + [-1], jks)
    for i in xrange(1, aj):
        if jks[i][0] == jks[i - 1][1]:
            jks[i - 1][1] = jks[i][1]
            jks[i][2] = 0
    jks = filter(lambda x: x[2] < 0, jks)
    jtime = reduce(lambda x, y: x - y[1] + y[0], jks, 720)
    both = cds + jks
    both.sort()
    both.append([both[0][0] + 1440, both[0][1] + 1440, both[0][2]])

    start = both[0][0]
    both = map(lambda x: [x[0] - start, x[1] - start, x[2]], both)

    for i in xrange(len(both) - 1):
        if both[i][2] == both[i + 1][2]:
            tt = both[i + 1][0] - both[i][1]
            both[i].append(tt)
        else:
            both[i].append(3600)
    both[-1].append(3600)

    cds = filter(lambda x: x[2] > 0, both)
    cds.sort(key=lambda x: x[3])
    for i in xrange(len(cds) - 1):
        if cds[i][3] <= ctime:
            ctime -= cds[i][3]
            cds[i][1] += cds[i][3]
            cds[i][3] = 0
    jks = filter(lambda x: x[2] < 0, both)
    jks.sort(key=lambda x: x[3])
    for i in xrange(len(jks) - 1):
        if jks[i][3] <= jtime:
            jtime -= jks[i][3]
            jks[i][1] += jks[i][3]
            jks[i][3] = 0
    both = cds + jks
    both.sort()

    result = 0
    for i in xrange(len(both) - 1):
        if both[i][2] == both[i + 1][2]:
            if both[i][1] == both[i + 1][0]:
                both[i + 1][0] = both[i][0]
                both[i][2] = 0
    both = filter(lambda x: x[2] != 0, both)

    for i in xrange(len(both) - 1):
        tt = both[i + 1][0] - both[i][1]
        if both[i][2] > 0:
            if tt <= ctime:
                ctime -= tt
                result += 1
            elif tt <= ctime + jtime:
                jtime -= (tt - ctime)
                ctime = 0
                if both[i][2] == both[i + 1][2]:
                    result += 2
                else:
                    result += 1
        else:
            if tt <= jtime:
                jtime -= tt
                result += 1
            elif tt <= ctime + jtime:
                ctime -= (tt - jtime)
                jtime = 0
                if both[i][2] == both[i + 1][2]:
                    result += 2
                else:
                    result += 1
    return result


if __name__ == "__main__":
    t = read_int()
    for test in xrange(1, t + 1):
        ac, aj = read_many_ints()
        print "Case #{}: {}".format(test, solve(ac, aj))
    exit(0)
