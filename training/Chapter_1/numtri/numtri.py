"""
ID: warreng1
LANG: PYTHON3
TASK: numtri
"""
with open('numtri.in', 'r') as fin:
    R = int(fin.readline())
    trilist = []
    for i in range(R):
        trilist.append(list(map(int, fin.readline().split())))
totals = []
maketri = []
for i in range(len(trilist)):
    if i == 0:
        maketri.append(trilist[i])
        continue
    appendlist = []
    for j in range(i+1):
        if j == i:
            appendlist.append(trilist[i][j]+maketri[i-1][j-1])
        elif j == 0:
            appendlist.append(trilist[i][j]+maketri[i-1][j])
        else:
            maketritemp = [maketri[i-1][j-1], maketri[i-1][j]]
            appendlist.append(trilist[i][j]+max(maketritemp))
    maketri.append(appendlist)
with open('numtri.out', 'w') as fout:
    print(max(maketri[-1]), file=fout)