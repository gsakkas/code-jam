from itertools import product


def read_int():
    return int(raw_input())


def read_many_ints():
    return map(int, raw_input().split())


def read_many(n):
    return [raw_input() for _ in xrange(n)]


def solve(n, ll):
    words = read_many(n)
    if ll == 1:
        return '-'
    letters = [sorted(list(set([w[i] for w in words])))
               for i in xrange(len(words[0]))]
    if reduce(lambda x, y: x and y,
              map(lambda x: x == letters[0],
                  letters)) and n == len(letters[0]) ** ll:
        return '-'
    words = set(words)
    for w in product(*letters):
        if ''.join(w) not in words:
            return ''.join(w)
    return '-'


if __name__ == "__main__":
    t = read_int()
    for test in xrange(1, t + 1):
        n, ll = read_many_ints()
        print "Case #{}: {}".format(test, solve(n, ll))
    exit(0)
