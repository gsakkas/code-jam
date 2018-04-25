fin = open('C-large-practice.in', 'r')
T = fin.readline().strip()
T = int(T)
fout = open('C-large-1c-practice.out', 'w')


for t in range(1, T + 1):
    line = fin.readline().split()
    fs = {}
    st = {}
    ft = {}
    answers = []
    answer = ['1', '1', '1']
    while int(answer[0] + answer[1] + answer[2]) <= int(line[0] + line[1] + line[2]):
        flag = [False] * 3
        flag2 = [False] * 3
        if answer[0] + answer[1] in fs.keys():
            flag2[0] = True
            if fs[answer[0] + answer[1]] < int(line[3]):
                flag[0] = True
        else:
            flag[0] = True
        if answer[1] + answer[2] in st.keys():
            flag2[1] = True
            if st[answer[1] + answer[2]] < int(line[3]):
                flag[1] = True
        else:
            flag[1] = True
        if answer[0] + answer[2] in ft.keys():
            flag2[2] = True
            if ft[answer[0] + answer[2]] < int(line[3]):
                flag[2] = True
        else:
            flag[2] = True

        if flag[0] and flag[1] and flag[2]:
            if flag2[0]:
                fs[answer[0] + answer[1]] += 1
            else:
                fs[answer[0] + answer[1]] = 1
            if flag2[1]:
                st[answer[1] + answer[2]] += 1
            else:
                st[answer[1] + answer[2]] = 1
            if flag2[2]:
                ft[answer[0] + answer[2]] += 1
            else:
                ft[answer[0] + answer[2]] = 1
            answers.append(' '.join(answer))
        if int(answer[2]) < int(line[2]):
            answer[2] = str(int(answer[2]) + 1)
        elif int(answer[1]) < int(line[1]):
            answer[1] = str(int(answer[1]) + 1)
            answer[2] = '1'
        else:
            answer[0] = str(int(answer[0]) + 1)
            answer[1] = '1'
            answer[2] = '1'
    fout.write('Case #{0}: {1}\n'.format(t, len(answers)))
    fout.write('\n'.join(answers))
    fout.write('\n')

fin.close()
fout.close()
