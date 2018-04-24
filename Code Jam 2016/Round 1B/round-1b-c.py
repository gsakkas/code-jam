fin = open('C-small.in', 'r')
T = fin.readline().strip()
T = int(T)
fout = open('C-small-1b.out', 'w')


def solve(counting, start, n, lines1, flags1):
    last_counting = 0
    for idx in range(start, n):
        if firsts[lines1[idx][0]] > 1 and lasts[lines1[idx][1]] > 1:
            right = 0
            left = 0
            for j in range(n):
                if not flags1[j] and lines1[j][0] == lines1[idx][0]:
                    right += 1
                elif not flags1[j] and lines1[j][1] == lines1[idx][1]:
                    left += 1
            if right >= 1 and left >= 1:
                last_counting = max(solve(counting, idx, n, lines1, flags1))
                counting += 1
                firsts[lines1[idx][0]] -= 1
                lasts[lines1[idx][1]] -= 1
                flags1[idx] = True
    return max(counting, last_counting)


for t in range(1, T + 1):
    N = fin.readline().strip()
    N = int(N)
    lines = []
    flags = [False] * N
    firsts = {}
    lasts = {}
    for i in range(1, N + 1):
        line = fin.readline().split()
        if line[0] not in firsts.keys():
            firsts[line[0]] = 1
        else:
            firsts[line[0]] += 1
        if line[1] not in lasts.keys():
            lasts[line[1]] = 1
        else:
            lasts[line[1]] += 1
        lines.append(line)

    count = solve(0, 0, N, lines, flags)

    fout.write('Case #{0}: {1}\n'.format(t, count))

fin.close()
fout.close()
