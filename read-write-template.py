fin = open('A-small-practice.in', 'r')
L, D, N = fin.readline().split()
L = int(L)
D = int(D)
N = int(N)
fout = open('A-small-qr-2009.out', 'w')

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
