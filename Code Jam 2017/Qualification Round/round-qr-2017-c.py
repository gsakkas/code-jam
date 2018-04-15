T = int(raw_input())
for t in xrange(1, T + 1):
    n, k = map(int, raw_input().split())
    people = 1
    batch = 1
    l_width = (n - 1) // 2
    r_width = n - l_width - 1
    # print people, l_width, r_width
    while people < k:
        l_width = (r_width - 1) // 2
        r_width = r_width - l_width - 1
        batch *= 2
        people = batch + people
        # print people, l_width, r_width
    if people // 2 + 1 == k:
        print 'Case #{0}: {1} {2}'.format(t, r_width, l_width)
    elif people == k:
        print 'Case #{0}: {1} {2}'.format(t, r_width - 1, l_width)
    else:
        print 'Case #{0}: {1} {2}'.format(t, r_width, l_width)
