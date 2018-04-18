# Old solution and partially wrong

fin = open('C-tiny.in', 'r')
T = fin.readline().strip()
T = int(T)
fout = open('C-tiny.out', 'w')

for t in range(1, T + 1):
    N = fin.readline().strip()
    N = int(N)
    line = fin.readline().split()
    maxed = 0
    for idx in range(N):
        bffs = {idx: int(line[idx]) - 1}
        j = bffs[idx]
        count = 1
        prev = idx
        while j not in bffs.keys() and int(line[j]) - 1 not in bffs.values():
            bffs[j] = int(line[j]) - 1
            prev = j
            j = bffs[prev]
            count += 1
        if j in bffs.keys() and j == idx and maxed < count:
            maxed = count
        elif int(line[j]) - 1 in bffs.values() and \
                int(line[j]) - 1 == prev and maxed < count:
            maxed = count + 1

    fout.write('Case #{0}: {1}\n'.format(t, maxed))

fin.close()
fout.close()
