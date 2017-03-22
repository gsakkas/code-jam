#!/usr/bin/env python

import sys

fin = open(sys.argv[1], 'r')
L, D, N = map(int, fin.readline().split())
fout = open(sys.argv[2], 'w')

print(L, D, N)
for d in range(1, D + 1):
    line = fin.readline().strip()
    print(line)

for n in range(1, N + 1):
    line = fin.readline().strip()
    print(line)
    fout.write('Case #{0}: {1}\n'.format(n, n / 2))

fin.close()
fout.close()
