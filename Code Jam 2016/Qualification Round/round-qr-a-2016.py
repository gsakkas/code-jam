fin = open('A-large.in', 'r')
T = fin.readline().strip()
T = int(T)
fout = open('A-large-qr.out', 'w')

for t in range(1, T + 1):
	line = fin.readline().strip()
	N = int(line)
	mysum = N
	fout.write('Case #{0}: '.format(t))
	if N == 0:
		fout.write('INSOMNIA\n')
		continue
	digits = []
	for idx in range(len(line)):
		if int(line[idx]) not in digits:
			digits.append(int(line[idx]))
	while len(digits) != 10:
		mysum += N
		line = str(mysum)
		for idx in range(len(line)):
			if int(line[idx]) not in digits:
				digits.append(int(line[idx]))
	if len(digits) == 10:
		fout.write(str(mysum) + '\n')
	else:
		fout.write('INSOMNIA\n')
fin.close()
fout.close()
