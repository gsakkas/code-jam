import re

fin = open('A-large-practice.in', 'r')
T = int(fin.readline())
fout = open('A-large-1b-2010.out', 'w')

directories = {}
for t in range(1, T+1):
	N, M = fin.readline().split()
	N = int(N)
	M = int(M)
	directories.clear()
	for n in range(1, N+1):
		directories[fin.readline().strip()] = 1
	directories['/'] = 1

	count = 0
	for m in range(1, M+1):
		directory = fin.readline().strip()
		if directory not in directories:
			directories[directory] = 1
			directory = directory.strip('/')
			path = directory.split('/')
			size = len(path)
			commands = 1
			while size - commands >= 0:
				temp = path[:size-commands]
				temp = '/'.join(temp)
				temp = '/' + temp
				if temp in directories:
					count += commands
					break
				else:
					directories[temp] = 1
					commands += 1
	fout.write('Case #{0}: {1}\n'.format(t, count))

fin.close()
fout.close()
