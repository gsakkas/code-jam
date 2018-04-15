T = int(raw_input())
for t in xrange(1, T + 1):
    n, M = map(int, raw_input().split())
    xs = 0
    os = 0
    ps = 0
    index = 0
    plus_idxs = []
    for m in xrange(M):
        symbol, x, y = raw_input().split()
        x = int(x)
        y = int(y)
        if symbol == 'o':
            os += 1
            index = y
        elif symbol == 'x':
            xs += 1
            index = y
        else:
            ps += 1
            plus_idxs.append(y)

    points = os * 2 + xs + ps
    solution = []
    if xs > 0:
        points += 1
        xs -= 1
        solution.append(('o', 1, index))
    elif xs == 0 and os == 0:
        index = 1
        if index in plus_idxs:
            points += 1
            ps -= 1
        else:
            points += 2
        solution.append(('o', 1, index))

    plus_idxs.append(index)
    for i in xrange(1, n + 1):
        if i not in plus_idxs:
            points += 1
            solution.append(('+', 1, i))
        if n > 2 and i != 1 and i != n:
            points += 1
            solution.append(('+', n, i))

    for i in xrange(2, n + 1):
        if index != i:
            points += 1
            solution.append(('x', i, i))

    if index != 1 and n > 1:
        points += 1
        solution.append(('x', index, 1))

    for p in solution:
        if p[0] == 'x':
            xs += 1
        elif p[0] == '+':
            ps += 1
        else:
            os += 1

    print 'Case #{0}: {1} {2}'.format(t, points, len(solution))
    for sol in solution:
        print '{0} {1} {2}'.format(*sol)
