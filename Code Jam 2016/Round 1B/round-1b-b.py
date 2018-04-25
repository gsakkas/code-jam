def read_int():
    return int(raw_input())


def read_many():
    return raw_input().split()


def choose(x):
    if x[0] == x[1] == '?':
        return '0'
    elif x[0] == x[1]:
        return x[0]
    elif x[0] != '?':
        return x[0]
    else:
        return x[1]


def solve():
    c, j = read_many()
    if filter(lambda x: x[0] != x[1] if x[0] != '?' and x[1] != '?' else False,
              zip(c, j)) == []:
        res = ''.join(map(choose, zip(c, j)))
        return res + ' ' + res
    cf = c[:]
    jf = j[:]
    ct = ''
    jt = ''
    diff = 10 ** 18 + 1
    for i in xrange(len(c)):
        if c[i] != j[i] and c[i] != '?' and j[i] != '?':
            if c[i] > j[i]:
                ct = c[:(i + 1)]
                ct += ''.join(map(lambda x: '0' if x ==
                                  '?' else x, c[(i + 1):]))
                jt = j[:(i + 1)]
                jt += ''.join(map(lambda x: '9' if x ==
                                  '?' else x, j[(i + 1):]))
            else:
                jt = j[:(i + 1)]
                jt += ''.join(map(lambda x: '0' if x ==
                                  '?' else x, j[(i + 1):]))
                ct = c[:(i + 1)]
                ct += ''.join(map(lambda x: '9' if x ==
                                  '?' else x, c[(i + 1):]))
            if abs(int(ct) - int(jt)) <= diff:
                diff = abs(int(ct) - int(jt))
                cf = ct
                jf = jt
            break
        elif c[i] == '?' and j[i] != '?':
            if j[i] != '9':
                ct = c[:i] + str(int(j[i]) + 1)
                ct += ''.join(map(lambda x: '0' if x ==
                                  '?' else x, c[(i + 1):]))
                jt = j[:(i + 1)]
                jt += ''.join(map(lambda x: '9' if x ==
                                  '?' else x, j[(i + 1):]))
                if abs(int(ct) - int(jt)) <= diff:
                    diff = abs(int(ct) - int(jt))
                    cf = ct
                    jf = jt
            if j[i] != '0':
                ct = c[:i] + str(int(j[i]) - 1)
                ct += ''.join(map(lambda x: '9' if x ==
                                  '?' else x, c[(i + 1):]))
                jt = j[:(i + 1)]
                jt += ''.join(map(lambda x: '0' if x ==
                                  '?' else x, j[(i + 1):]))
                if abs(int(ct) - int(jt)) <= diff:
                    diff = abs(int(ct) - int(jt))
                    cf = ct
                    jf = jt
            c = c[:i] + j[i] + c[(i + 1):]
        elif j[i] == '?' and c[i] != '?':
            if c[i] != '9':
                jt = j[:i] + str(int(c[i]) + 1)
                jt += ''.join(map(lambda x: '0' if x ==
                                  '?' else x, j[(i + 1):]))
                ct = c[:(i + 1)]
                ct += ''.join(map(lambda x: '9' if x ==
                                  '?' else x, c[(i + 1):]))
                if abs(int(ct) - int(jt)) <= diff:
                    diff = abs(int(ct) - int(jt))
                    cf = ct
                    jf = jt
            if c[i] != '0':
                jt = j[:i] + str(int(c[i]) - 1)
                jt += ''.join(map(lambda x: '9' if x ==
                                  '?' else x, j[(i + 1):]))
                ct = c[:(i + 1)]
                ct += ''.join(map(lambda x: '0' if x ==
                                  '?' else x, c[(i + 1):]))
                if abs(int(ct) - int(jt)) <= diff:
                    diff = abs(int(ct) - int(jt))
                    cf = ct
                    jf = jt
            j = j[:i] + c[i] + j[(i + 1):]
        elif c[i] == j[i] == '?':
            ct = c[:i] + '0'
            ct += ''.join(map(lambda x: '9' if x == '?' else x, c[(i + 1):]))
            jt = j[:i] + '1'
            jt += ''.join(map(lambda x: '0' if x == '?' else x, j[(i + 1):]))
            if abs(int(ct) - int(jt)) <= diff:
                diff = abs(int(ct) - int(jt))
                cf = ct
                jf = jt
            ct = c[:i] + '1'
            ct += ''.join(map(lambda x: '0' if x == '?' else x, c[(i + 1):]))
            jt = j[:i] + '0'
            jt += ''.join(map(lambda x: '9' if x == '?' else x, j[(i + 1):]))
            if abs(int(ct) - int(jt)) <= diff:
                diff = abs(int(ct) - int(jt))
                cf = ct
                jf = jt
            c = c[:i] + '0' + c[(i + 1):]
            j = j[:i] + '0' + j[(i + 1):]
    return cf + ' ' + jf


if __name__ == "__main__":
    t = read_int()
    for test in xrange(1, t + 1):
        print "Case #{}: {}".format(test, solve())
    exit(0)
