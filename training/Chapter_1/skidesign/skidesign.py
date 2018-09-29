"""
ID: warreng1
LANG: PYTHON3
TASK: skidesign
"""
with open('skidesign.in', 'r') as fin:
    N = int(fin.readline())
    hills = sorted(list(map(int, [fin.readline().rstrip() for i in range(N)])))

getRidOf = (max(hills)-min(hills))-17

# Make a list called HMA, this means HILLS, MONEY, AMOUNT TO ADD NEXT.
HMA = [[i, 0, 1] for i in hills]
money = 0
# Use getRidOf/2 and change the smaller side of the hills.  If there is a remainder, use on the top.
while getRidOf != 0:
    smallest = [0]
    biggest = [N-1]

    for i in range(1, len(HMA)):
        if HMA[i][0] == HMA[smallest[0]][0]:
            smallest.append(i)
        else:
            break

    REVERSEhma = HMA[::-1]
    for i in range(1, len(HMA)):
        if HMA[i][0] == HMA[biggest[0]][0]:
            biggest.append(i)
        else:
            break
    money = 0
    print(HMA)
    getRidOf -= 1