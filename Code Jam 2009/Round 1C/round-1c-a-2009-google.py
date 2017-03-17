# This is a proposed solution from Google
fin = open('A-small-practice.in', 'r')
fout = open('A-small-1c-2009.out', 'w')
N = int(fin.readline().strip())
for qw in range(1, N + 1):
    num = fin.readline().strip()
    values = {num[0]: 1}
    for c in num:
        if c not in values:
            sz = len(values)
            if sz == 1:
                values[c] = 0
            else:
                values[c] = sz
    result = 0
    base = max(len(values), 2)
    for c in num:
        result *= base
        result += values[c]
    fout.write('Case #{0}: {1}\n'.format(str(qw), str(result)))

fin.close()
fout.close()
