"""
ID: warreng1
LANG: PYTHON3
TASK: ariprog
"""
with open('ariprog.in', 'r') as fin:
    N = int(fin.readline())
    M = int(fin.readline())

squarelist = [0, 1]
for i in range(1, M):
    squarelist.append(squarelist[i]+1+(i+i))

squares = []
for p in squarelist:
    for q in squarelist:
        if p+q not in squares:
            squares.append(p+q)
squares.sort()
finalans = []
for i in range(len(squares)):
    for j in range(len(squares)):
        curgap = squares[j]-squares[i]
        if curgap == 0:
            continue
        newnum = squares[i]
        if curgap > 0:
            for k in range(1, N):
                if newnum+k*curgap not in squares:
                    break
                if k == N-1:
                    finalans.append([squares[i], curgap])
finalans.sort(key=lambda x: x[1])
with open('ariprog.out', 'w') as fout:
    if finalans != []:
        for i in finalans:
            print(i[0], i[1], file=fout)
    else:
        print('NONE', file=fout)