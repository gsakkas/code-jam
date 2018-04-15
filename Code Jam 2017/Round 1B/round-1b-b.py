# Works only for small testset

T = int(raw_input())
for t in xrange(1, T + 1):
    n, r, o, y, g, b, v = map(int, raw_input().split())
    sol = ""
    if o == 0 and g == 0 and v == 0:
        if r == y and y == b:
            sol = "RYB" * r
        else:
            mxx = max(r, y, b)
            if r == mxx and y + b >= r:
                turn = True if max(y, b) == y else False
                while r > 0:
                    r -= 1
                    if turn and y > 0:
                        sol += "RY"
                        y -= 1
                    elif not turn and b > 0:
                        sol += "RB"
                        b -= 1

                    if y == 0:
                        turn = False
                    elif b == 0:
                        turn = True
                    else:
                        turn = not turn
                while y > 0 or b > 0:
                    temp = ""
                    while sol:
                        if sol[1] == "Y" and b > 0:
                            b -= 1
                            temp += sol[:2] + "B"
                            sol = sol[2:]
                        elif sol[1] == "B" and y > 0:
                            y -= 1
                            temp += sol[:2] + "Y"
                            sol = sol[2:]
                        elif sol[1] == "Y" and b == 0:
                            temp += sol[:2]
                            sol = sol[2:]
                        elif sol[1] == "B" and y == 0:
                            temp += sol[:2]
                            sol = sol[2:]
                    sol = temp
            elif y == mxx and r + b >= y:
                turn = True if max(r, b) == r else False
                while y > 0:
                    y -= 1
                    if turn and r > 0:
                        sol += "YR"
                        r -= 1
                    elif not turn and b > 0:
                        sol += "YB"
                        b -= 1

                    if r == 0:
                        turn = False
                    elif b == 0:
                        turn = True
                    else:
                        turn = not turn
                while r > 0 or b > 0:
                    temp = ""
                    while sol:
                        if sol[1] == "R" and b > 0:
                            b -= 1
                            temp += sol[:2] + "B"
                            sol = sol[2:]
                        elif sol[1] == "B" and r > 0:
                            r -= 1
                            temp += sol[:2] + "R"
                            sol = sol[2:]
                        elif sol[1] == "R" and b == 0:
                            temp += sol[:2]
                            sol = sol[2:]
                        elif sol[1] == "B" and r == 0:
                            temp += sol[:2]
                            sol = sol[2:]
                    sol = temp
            elif b == mxx and y + r >= b:
                turn = True if max(y, r) == y else False
                while b > 0:
                    b -= 1
                    if turn and y > 0:
                        sol += "BY"
                        y -= 1
                    elif not turn and r > 0:
                        sol += "BR"
                        r -= 1

                    if y == 0:
                        turn = False
                    elif r == 0:
                        turn = True
                    else:
                        turn = not turn
                while y > 0 or r > 0:
                    temp = ""
                    while sol:
                        if sol[1] == "Y" and r > 0:
                            r -= 1
                            temp += sol[:2] + "R"
                            sol = sol[2:]
                        elif sol[1] == "R" and y > 0:
                            y -= 1
                            temp += sol[:2] + "Y"
                            sol = sol[2:]
                        elif sol[1] == "Y" and r == 0:
                            temp += sol[:2]
                            sol = sol[2:]
                        elif sol[1] == "R" and y == 0:
                            temp += sol[:2]
                            sol = sol[2:]
                    sol = temp
    else:
        if g == v and v == o:
            sol = "GVO" * g
        else:
            mxx = max(g, v, o)
            if g == mxx:
                turn = True if max(v, o) == v else False
                while g > 0:
                    g -= 1
                    if turn and v > 0:
                        sol += "GV"
                        v -= 1
                    elif not turn and o > 0:
                        sol += "GO"
                        o -= 1
                    elif v == 0 and o == 0:
                        sol += "G"

                    if v == 0:
                        turn = False
                    elif o == 0:
                        turn = True
                    else:
                        turn = not turn
                while v > 0 or o > 0:
                    temp = ""
                    while sol:
                        if sol[1] == "V" and o > 0:
                            o -= 1
                            temp += sol[:2] + "O"
                            sol = sol[2:]
                        elif sol[1] == "O" and v > 0:
                            v -= 1
                            temp += sol[:2] + "V"
                            sol = sol[2:]
                        elif sol[1] == "V" and o == 0:
                            temp += sol[:2]
                            sol = sol[2:]
                        elif sol[1] == "O" and v == 0:
                            temp += sol[:2]
                            sol = sol[2:]
                    sol = temp
            elif v == mxx:
                turn = True if max(g, o) == g else False
                while v > 0:
                    v -= 1
                    if turn and g > 0:
                        sol += "VG"
                        g -= 1
                    elif not turn and o > 0:
                        sol += "VO"
                        o -= 1
                    elif g == 0 and o == 0:
                        sol += "V"

                    if g == 0:
                        turn = False
                    elif o == 0:
                        turn = True
                    else:
                        turn = not turn
                while g > 0 or o > 0:
                    temp = ""
                    while sol:
                        if sol[1] == "G" and o > 0:
                            o -= 1
                            temp += sol[:2] + "O"
                            sol = sol[2:]
                        elif sol[1] == "O" and g > 0:
                            g -= 1
                            temp += sol[:2] + "G"
                            sol = sol[2:]
                        elif sol[1] == "G" and o == 0:
                            temp += sol[:2]
                            sol = sol[2:]
                        elif sol[1] == "O" and g == 0:
                            temp += sol[:2]
                            sol = sol[2:]
                    sol = temp
            elif o == mxx:
                turn = True if max(v, g) == v else False
                while o > 0:
                    o -= 1
                    if turn and v > 0:
                        sol += "OV"
                        v -= 1
                    elif not turn and g > 0:
                        sol += "OG"
                        g -= 1
                    elif g == 0 and v == 0:
                        sol += "O"

                    if v == 0:
                        turn = False
                    elif g == 0:
                        turn = True
                    else:
                        turn = not turn
                while v > 0 or g > 0:
                    temp = ""
                    while sol:
                        if sol[1] == "V" and g > 0:
                            g -= 1
                            temp += sol[:2] + "G"
                            sol = sol[2:]
                        elif sol[1] == "G" and v > 0:
                            v -= 1
                            temp += sol[:2] + "V"
                            sol = sol[2:]
                        elif sol[1] == "V" and g == 0:
                            temp += sol[:2]
                            sol = sol[2:]
                        elif sol[1] == "G" and v == 0:
                            temp += sol[:2]
                            sol = sol[2:]
                    sol = temp
        if y > 0:
            i = 0
            temp = ""
            while i < len(sol):
                if i < len(sol):
                    if sol[i] == "V":
                        if i + 1 < len(sol):
                            if sol[i + 1] == "V":
                                y -= 1
                                temp += "Y" + sol[i]
                            elif y > 1:
                                y -= 2
                                temp += "Y" + sol[i] + "Y" + sol[i + 1]
                                i += 1
                        else:
                            if sol[0] == "V":
                                y -= 1
                                temp += "Y" + sol[i]
                i += 1
            sol = temp

        if b > 0:
            i = 0
            temp = ""
            while i < len(sol):
                if i < len(sol):
                    if sol[i] == "O":
                        if i + 1 < len(sol):
                            if sol[i + 1] == "O":
                                b -= 1
                                temp += "B" + sol[i]
                            elif b > 1:
                                b -= 2
                                temp += "B" + sol[i] + "B" + sol[i + 1]
                                i += 1
                        else:
                            if sol[0] == "O":
                                b -= 1
                                temp += "B" + sol[i]
                i += 1
            sol = temp

        if r > 0:
            i = 0
            temp = ""
            while i < len(sol):
                if i < len(sol):
                    if sol[i] == "G":
                        if i + 1 < len(sol):
                            if sol[i + 1] == "G":
                                r -= 1
                                temp += "R" + sol[i]
                            elif r > 1:
                                r -= 2
                                temp += "R" + sol[i] + "R" + sol[i + 1]
                                i += 1
                        else:
                            if sol[0] == "G":
                                r -= 1
                                temp += "R" + sol[i]
                i += 1
            sol = temp

    if sol:
        print 'Case #{0}: {1}'.format(t, sol)
    else:
        print 'Case #{0}: IMPOSSIBLE'.format(t)
