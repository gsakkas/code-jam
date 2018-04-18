def read_int():
    return int(raw_input())


def solve(s):
    result = s[0]
    for sub in s[1:]:
        if sub < result[0]:
            result += sub
        else:
            result = sub + result
    return result


if __name__ == "__main__":
    t = read_int()
    for test in xrange(1, t + 1):
        s = raw_input()
        print "Case #{}: {}".format(test, solve(s))
    exit(0)
