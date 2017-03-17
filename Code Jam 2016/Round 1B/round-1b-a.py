fin = open('A-large.in', 'r')
T = fin.readline().strip()
T = int(T)
fout = open('A-large-1b.out', 'w')

nums = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

for t in range(1, T + 1):
	line = fin.readline().strip()
	answer = []
	while True:
		if 'Z' in line:
			answer.append('0')
			for i in range(len(nums[0])):
				idx = line.find(nums[0][i])
				line = line[:idx] + line[idx+1:]
		elif 'W' in line:
			answer.append('2')
			for i in range(len(nums[2])):
				idx = line.find(nums[2][i])
				line = line[:idx] + line[idx+1:]
		elif 'U' in line:
			answer.append('4')
			for i in range(len(nums[4])):
				idx = line.find(nums[4][i])
				line = line[:idx] + line[idx+1:]
		elif 'X' in line:
			answer.append('6')
			for i in range(len(nums[6])):
				idx = line.find(nums[6][i])
				line = line[:idx] + line[idx+1:]
		elif 'G' in line:
			answer.append('8')
			for i in range(len(nums[8])):
				idx = line.find(nums[8][i])
				line = line[:idx] + line[idx+1:]
		else:
			break

	while True:
		if 'O' in line and 'N' in line and 'E' in line:
			answer.append('1')
			for i in range(len(nums[1])):
				idx = line.find(nums[1][i])
				line = line[:idx] + line[idx+1:]
		elif 'T' in line and 'H' in line and 'R' in line and line.count('E') >= 2:
			answer.append('3')
			for i in range(len(nums[3])):
				idx = line.find(nums[3][i])
				line = line[:idx] + line[idx+1:]
		elif 'F' in line and 'I' in line and 'V' in line and 'E' in line:
			answer.append('5')
			for i in range(len(nums[5])):
				idx = line.find(nums[5][i])
				line = line[:idx] + line[idx+1:]
		elif 'S' in line and 'V' in line and 'N' in line and line.count('E') >= 2:
			answer.append('7')
			for i in range(len(nums[7])):
				idx = line.find(nums[7][i])
				line = line[:idx] + line[idx+1:]
		elif 'N' in line and 'I' in line and 'N' in line and 'E' in line:
			answer.append('9')
			for i in range(len(nums[9])):
				idx = line.find(nums[9][i])
				line = line[:idx] + line[idx+1:]
		else:
			break

	answer.sort()
	final = ''.join(answer)
	fout.write('Case #{0}: {1}\n'.format(t, final))

fin.close()
fout.close()
