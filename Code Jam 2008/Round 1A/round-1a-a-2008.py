fin = open('A-large-practice.in', 'r')
T = int(fin.readline())
fout = open('A-large-1a-2008.out', 'w')

for t in range(1, T + 1):
    N = int(fin.readline())
    # First way of reading integers
    x = list(map(int, fin.readline().split()))
    # Second way of reading integers
    y = [int(yi) for yi in fin.readline().split()]
    x.sort()
    y.sort()
    count = 0
    while len(x) > 0:
        count += x[0] * y[-1]
        x.pop(0)
        y.pop()

    fout.write('Case #{0}: {1}\n'.format(t, count))

fin.close()
fout.close()
