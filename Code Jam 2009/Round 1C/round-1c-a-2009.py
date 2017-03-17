fin = open('A-large-practice.in', 'r')
T = int(fin.readline())
lines = fin.read().splitlines()
fin.close()
fout = open('A-large-1c-2009.out', 'w')

dictio = {}
encoding = {}

for count, line in enumerate(lines, start=1):
	base = 0
	chars = 0
	encoding.clear()
	dictio.clear()
	for ch in line:
		if ch not in dictio:
			base += 1
			dictio[ch] = 1
		chars += 1

	if base < 2:
		base = 2

	power = chars
	last_num = 1
	seconds = 0
	for ch in line:
		power -= 1
		if ch in encoding.keys():
			seconds += encoding[ch] * (base ** power)
		else:
			encoding[ch] = last_num
			if last_num > 1:
				last_num += 1
			elif last_num == 1:
				last_num = 0
			elif last_num == 0:
				last_num = 2
			else:
				last_num = 0
			seconds += encoding[ch] * (base ** power)
	fout.write('Case #{0}: {1}\n'.format(str(count), str(seconds)))

fout.close()
