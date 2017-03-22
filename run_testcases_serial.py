# The serial version of the "run_testcases_parallel.py".
# Use this to check the speedup on your PC.


def solve(k):
    sum = 0
    for i in xrange(1000000):
        sum += k
        sum %= 123444
    return sum


T = int(raw_input())
processes = []
for t in range(1, T + 1):
    data = int(raw_input())
    res = solve(data)
    print('Case #{0}: {1}'.format(t, res))
