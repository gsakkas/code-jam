import itertools


def is_prime(n):
	if n == 2 or n == 3:
		return -1
	if n < 2 or n % 2 == 0:
		return 2
	if n < 9:
		return -1
	if n % 3 == 0:
		return 3
	r = 20000
	dia = 5
	while dia <= r:
		if n % dia == 0:
			return dia
		if n % (dia + 2) == 0:
			return dia + 2
		dia += 6
	return -1


fin = open('C-large.in', 'r')
T = fin.readline().strip()
T = int(T)
fout = open('C-large-qr.out', 'w')

for t in range(1, T + 1):
	line = fin.readline().split()
	fout.write('Case #{0}:\n'.format(t))
	iterator = itertools.count()
	count = 0
	for num in iterator:
		big_numb = "%030d" % (int(bin(num)[2:]),)
		big_numb = '1{0}1'.format(big_numb)
		divisors = []
		for base in range(2, 11):
			mysum = 0
			temp_base = 1
			for idx in range(-1, -(int(line[0]) + 1), -1):
				mysum += int(big_numb[idx]) * temp_base
				temp_base *= base
			kalimera = is_prime(mysum)
			if kalimera > 0:
				divisors.append(kalimera)
			else:
				break
		if len(divisors) == 9:
			fout.write("{0} {1}\n".format(big_numb, " ".join(map(str, divisors))))
			count += 1
		if count == int(line[1]):
			break

fin.close()
fout.close()
