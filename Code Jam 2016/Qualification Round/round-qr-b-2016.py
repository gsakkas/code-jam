def change(x):
	if x == '-':
		return '+'
	else:
		return '-'

fin = open('B-large.in', 'r')
S = fin.readline().strip()
S = int(S)
fout = open('B-large-qr.out', 'w')

for s in range(1, S + 1):
	line = list(fin.readline().strip())
	count = 0
	last = len(line)-1
	while last != -1:
		while line[last] == '+':
			last -= 1
			if last == -1:
				break
		if last == -1:
			break
		first = 0
		while line[first] == '+':
			first += 1
			if first == len(line):
				break
		if first == len(line):
			break
		if first != 0:
			line = ['-']*first + line[first:]
			count += 1
		line = list(map(change, reversed(line[:(last+1)]))) + line[(last+1):]
		count += 1
	fout.write('Case #{0}: {1}\n'.format(s, count))

fin.close()
fout.close()
