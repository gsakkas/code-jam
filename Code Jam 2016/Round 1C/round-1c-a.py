from string import ascii_uppercase


def read_int():
    return int(raw_input())


def read_many_ints():
    return map(int, raw_input().split())


def char(i):
    return ascii_uppercase[i]


def sizes(senators, num_of_sens):
    return map(lambda x: float(x) * 100 / num_of_sens, senators)


def solve(n):
    senators = read_many_ints()
    solution = []
    num_of_sens = sum(senators)
    while len(filter(lambda x: x > 0, senators)) > 2:
        step = ""
        party = senators.index(max(senators))
        temp_sens = senators[:]
        temp_sens[party] -= 1
        if not filter(lambda x: x > 50, sizes(temp_sens, num_of_sens - 1)):
            step += char(party)
            solution.append(step)
            num_of_sens -= 1
            senators = temp_sens
    while num_of_sens:
        solution.append(
            reduce(lambda x, y: x + char(y[0]) if y[1] else x,
                   enumerate(senators), ""))
        num_of_sens -= 2
    return ' '.join(solution)


if __name__ == "__main__":
    t = read_int()
    for test in xrange(1, t + 1):
        n = read_int()
        print "Case #{}: {}".format(test, solve(n))
    exit(0)
