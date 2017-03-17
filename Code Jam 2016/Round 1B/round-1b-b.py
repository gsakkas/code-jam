fin = open('B-small-practice.in', 'r')
T = fin.readline().strip()
T = int(T)
fout = open('B-small-1b-practice.out', 'w')


for t in range(1, T + 1):
	line = list(map(list, fin.readline().split()))
	print(line)
	for i in range(len(line[0])):
		if line[0][i] == '?' and line[1][i] == '?':
			if i + 2 <= len(line[0]):
				if line[0][i+1] != '?' and line[1][i+1] != '?':
					if int(line[0][i+1]) == int(line[1][i+1]):
						line[0][i] = '0'
						line[1][i] = '0'
					elif abs(int(line[0][i+1]) - int(line[1][i+1])) < 5:
						line[0][i] = '0'
						line[1][i] = '0'
						if int(line[0][i+1]) < int(line[1][i+1]):
							for j in range(i, len(line[0])):
								if line[0][j] == '?':
									line[0][j] = '9'
								if line[1][j] == '?':
									line[1][j] = '0'
							break
						else:
							for j in range(i, len(line[0])):
								if line[0][j] == '?':
									line[0][j] = '0'
								if line[1][j] == '?':
									line[1][j] = '9'
							break
					elif abs(int(line[0][i+1]) - int(line[1][i+1])) > 5:
						if int(line[0][i+1]) < int(line[1][i+1]):
							line[0][i] = '1'
							line[1][i] = '0'
							for j in range(i, len(line[0])):
								if line[0][j] == '?':
									line[0][j] = '0'
								if line[1][j] == '?':
									line[1][j] = '9'
							break
						else:
							line[0][i] = '0'
							line[1][i] = '1'
							for j in range(i, len(line[0])):
								if line[0][j] == '?':
									line[0][j] = '9'
								if line[1][j] == '?':
									line[1][j] = '0'
							break
					else:
						if int(line[0][i+1]) < int(line[1][i+1]):
							for j in range(i, len(line[0])):
								if line[0][j] != '?':
									line[0][j] = '0'
								if line[1][j] != '?':
									line[1][j] = '9'
							break
						else:
							for j in range(i, len(line[0])):
								if line[0][j] == '?':
									line[0][j] = '9'
								if line[1][j] == '?':
									line[1][j] = '0'
							break
			else:
				line[0][i] = '0'
				line[1][i] = '0'
		elif line[0][i] == '?' or line[1][i] == '?':
			line[0][i] = '0'
			line[1][i] = '0'

	fout.write('Case #{0}: {1} {2}\n'.format(t, ''.join(line[0]), ''.join(line[1])))

fin.close()
fout.close()
