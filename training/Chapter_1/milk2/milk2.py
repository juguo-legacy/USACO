"""
ID: warreng1
LANG: PYTHON3
TASK: milk2
"""
alist = []
ansb = []
finala = [0]
finalb = [0]
con = 0
shouldcon = 0
iftrue = False
with open('milk2.in', 'r') as fin:
    number = int(fin.readline())
    for x in range(number):
        alist.append(list(map(int, fin.readline().split())))
alist = sorted(alist)
fout = open('milk2.out', 'w')
for x in range(len(alist)):
    if x != len(alist)-1:
        if alist[x][1] < alist[x+1][0]:
            ansb.append(alist[x])
            ansb.append(alist[x+1])
save = []
for x in range(len(alist)):
    finala.append(alist[x][1]-alist[x][0])
    if x != len(alist)-1:
        if alist[x][1] >= alist[x+1][0]:
            iftrue = True
            con += 1
            save.append(alist[x])
            print(save)
        if con > 0:
            shouldcon += 1
            if con != shouldcon:
                finala.append(alist[x][1]-save[0][0])
                save = []
                con = 0
    elif 1 == len(alist):
        finala.append(alist[x][1]-alist[x][0])
    elif x == len(alist)-1:
        if shouldcon == con:
            if iftrue:
                finala.append(alist[x][1]-save[0][0])
if ansb != []:
    for x in range(len(ansb)):
        if x != len(ansb)-1:
            if ansb[x][1] < ansb[x+1][0]:
                finalb.append(ansb[x+1][0]-ansb[x][1])
if alist[0][0] < alist[-1][0] and alist[0][1] >= alist[-1][1]:
    print('true')
    finalb = [0]
print('alist: ', alist)
print('finala: ', finala)
a = max(finala)
if ansb == []:
    b = 0
else:
    b = max(finalb)
print(a, b)
print(a, b, file=fout)
fout.close()
