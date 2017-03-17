def find_inters(l, ls):
    c = 0
    for i in range(l + 1, len(ls)):
        if (ls[l][0] > ls[i][0]) & (ls[l][1] < ls[i][1]):
            c += 1
        elif (ls[l][0] < ls[i][0]) & (ls[l][1] > ls[i][1]):
            c += 1
    return c


fin = open('A-large-practice.in', 'r')
T = int(fin.readline())
fout = open('A-large-1c-2010.out', 'w')

for t in range(1, T + 1):
    N = int(fin.readline())
    lines = []
    for n in range(1, N + 1):
        lines.append(list(map(int, fin.readline().split())))
    count = 0
    for line in range(len(lines)):
        count += find_inters(line, lines)
    fout.write('Case #{0}: {1}\n'.format(t, count))

fin.close()
fout.close()
