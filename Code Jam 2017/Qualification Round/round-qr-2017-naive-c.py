T = int(raw_input())
for t in xrange(1, T + 1):
    n, k = map(int, raw_input().split())
    widths = [n]
    num_of_width = {n: 1}
    l_width = (n - 1) / 2
    r_width = n - 1 - l_width

    max_w = n
    batch = 1

    while batch < k:
        k -= batch
        num_of_width.pop(max_w)
        widths.remove(max_w)

        if l_width in num_of_width:
            num_of_width[l_width] += batch
        else:
            num_of_width[l_width] = batch

        if l_width not in widths:
            widths.append(l_width)

        if r_width in num_of_width:
            num_of_width[r_width] += batch
        else:
            num_of_width[r_width] = batch

        if r_width not in widths:
            widths.append(r_width)

        max_w = max(widths)
        batch = num_of_width[max_w]

        l_width = (max_w - 1) / 2
        r_width = max_w - 1 - l_width

    print 'Case #{0}: {1} {2}'.format(t, r_width, l_width)
