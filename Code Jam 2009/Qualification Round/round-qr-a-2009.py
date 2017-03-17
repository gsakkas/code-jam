import re

fin = open('A-large-practice.in', 'r')
L, D, N = fin.readline().split()
L = int(L)
D = int(D)
N = int(N)
fout = open('A-large-qr-2009.out', 'w')

words = []
for d in range(1, D+1):
	line = fin.readline().strip()
	words.append(line)

words = ','.join(words)

for n in range(1, N+1):
	line = fin.readline().strip()
	line = line.replace('(', '[')
	line = line.replace(')', ']')
	count = len(re.findall(line, words))
	fout.write('Case #{0}: {1}\n'.format(n, count))

fin.close()
fout.close()
