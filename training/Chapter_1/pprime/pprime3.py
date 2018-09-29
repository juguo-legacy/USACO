"""
ID: warreng1
LANG: PYTHON3
TASK: pprime
"""
import math
with open('pprime.in', 'r') as fin:
    A, B = map(int, fin.readline().split())
finalans = []
if A % 2 == 0:
    A += 1
recurlist = list(map(str, range(10)))
def recurring(recurLEN, depth, recurlist):
    if recurLEN == depth:
        prev = recurring(recurLEN, depth-1, recurlist)
        newprev = []
        for i in range(1, 10, 2):
            for j in prev:
                newprev.append(str(i)+str(j)+str(i))
        return newprev
    elif depth == 0:
        return list(range(10))
    else:
        prev = recurring(recurLEN, depth-1, recurlist)
        newprev = []
        for i in range(10):
            for j in prev:
                newprev.append(str(i)+str(j)+str(i))
        return newprev

def evenpalin(palinLen):
    returnL = []
    for i in range(1*(10**((palinLen//2)-1)), 10*(10**((palinLen//2)-1))):
        returnL.append(str(i)+str(i)[::-1])
    return returnL

for i in range(2, len(str(B))+1):
    if i % 2 == 0:
        newl = evenpalin(i)
    else:
        newl = recurring(i//2, i//2, recurlist)
    recurlist = recurlist+newl

for i in recurlist:
    if int(i) % 2 == 0:
        continue
    if int(i) >= A and int(i) <= B:
        if int(i) == 5:
            finalans.append(5)
            continue
        elif int(i) == 7:
            finalans.append(7)
            continue
        ending = int(math.sqrt(int(i)))
        if ending % 2 == 0:
            ending += 1
        for j in range(3, ending+1, 2):
            if int(i)%j == 0:
                break
            elif j == ending:
                finalans.append(int(i))
    elif int(i) > B:
        break

with open('pprime.out', 'w') as fout:
    for i in range(len(finalans)):
        print(finalans[i], file=fout)