fin = open('D-large.in', 'r')
T = fin.readline().strip()
T = int(T)
fout = open('D-large-qr.out', 'w')


for t in range(1, T + 1):
	K, C, S = fin.readline().split()
	K = int(K)
	C = int(C)
	S = int(S)
	if K == S:
		pos = ' '.join(map(str, list(range(1, S + 1))))
		fout.write('Case #{0}: {1}\n'.format(t, pos))
	elif S*C < K:
		fout.write('Case #{0}: IMPOSSIBLE\n'.format(t))
	else:
		tiles = []
		for idx in range(1, K + 1, C):
			pos = 1
			for j in range(C):
				pos = (pos - 1) * K + min(idx + j, K)
			tiles.append(pos)
		pos = ' '.join(map(str, tiles))
		fout.write('Case #{0}: {1}\n'.format(t, pos))

fin.close()
fout.close()
