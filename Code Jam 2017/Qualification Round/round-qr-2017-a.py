def flip_k(data, k, start):
    if start + k > len(data):
        return data
    for i in xrange(start, start + k):
        data[i] = not data[i]
    return data


def check_happy(data):
    return reduce(lambda x, y: x and y, data)


T = int(raw_input())
for t in xrange(1, T + 1):
    data, k = raw_input().split()
    k = int(k)
    data = map(lambda x: True if x is '+' else False, data)
    prev = map(lambda x: not x, data)
    initial = prev[:]
    count = 0
    while (data != initial) and (data != prev):
        for i, pancake in enumerate(data):
            if not pancake:
                prev = data[:]
                data = flip_k(data, k, i)
                count += 1
            if check_happy(data):
                break
        if check_happy(data):
            break
    if check_happy(data):
        print 'Case #{0}: {1}'.format(t, count)
    else:
        print 'Case #{0}: IMPOSSIBLE'.format(t)
