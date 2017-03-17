fin = open('A-large-practice.in', 'r')
T = int(fin.readline())
fout = open('A-large-1a-2010.out', 'w')

for t in range(1, T + 1):
    N, K = map(int, fin.readline().split())
    board = []
    for n in range(0, N):
        temp = []
        for ch in fin.readline().split()[0]:
            temp.append(ch)
        board.append(temp)
        board[n] = [value for value in board[n] if value != '.']
        while len(board[n]) < N:
            board[n].insert(0, '.')
    # board = list(zip(*board[::-1])) Rotates 90 degrees the array
    for i in range(N):
        print(''.join(board[i]))
    print('-----------------------------------------------')
    blue = False
    red = False
    for i in range(N):
        for j in range(N):
            check = '.'
            if (board[i][j] == 'B') and (not blue):
                check = 'B'
            elif (board[i][j] == 'R') and (not red):
                check = 'R'
            if check != '.':
                k = 1
                pos = j + 1
                while (k < K) and (pos < N):
                    if board[i][pos] != check:
                        break
                    elif board[i][pos] == check:
                        pos += 1
                        k += 1
                if k == K:
                    if check == 'B':
                        blue = True
                    else:
                        red = True
                k = 1
                pos = i + 1
                while (k < K) and (pos < N):
                    if board[pos][j] != check:
                        break
                    elif board[pos][j] == check:
                        pos += 1
                        k += 1
                if k == K:
                    if check == 'B':
                        blue = True
                    else:
                        red = True
                k = 1
                posi = i + 1
                posj = j + 1
                while (k < K) and (posi < N) and (posj < N):
                    if board[posi][posj] != check:
                        break
                    elif board[posi][posj] == check:
                        posi += 1
                        posj += 1
                        k += 1
                if k == K:
                    if check == 'B':
                        blue = True
                    else:
                        red = True
                k = 1
                posi = i + 1
                posj = j - 1
                while (k < K) and (posi < N) and (posj >= 0):
                    if board[posi][posj] != check:
                        break
                    elif board[posi][posj] == check:
                        posi += 1
                        posj -= 1
                        k += 1
                if k == K:
                    if check == 'B':
                        blue = True
                    else:
                        red = True
    if red and blue:
        fout.write('Case #{0}: Both\n'.format(t))
    elif red:
        fout.write('Case #{0}: Red\n'.format(t))
    elif blue:
        fout.write('Case #{0}: Blue\n'.format(t))
    else:
        fout.write('Case #{0}: Neither\n'.format(t))

fin.close()
fout.close()
