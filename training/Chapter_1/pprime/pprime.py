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
    if A == 2:
        finalans.append(2)
    A += 1
possibles = ['1', '3', '7', '9']
for i in range(A, B+1, 2):
    if i == 5:
        finalans.append(5)
    elif i == 7:
        finalans.append(7)
    elif str(i)[-1] not in possibles:
        continue
    else:
        ending = int(math.sqrt(i))
        if ending % 2 == 0:
            ending += 1
        for j in range(3, ending+1, 2):
            if i%j == 0:
                break
            elif j == ending:
                if str(i) == str(i)[::-1]:
                    finalans.append(i)
with open('pprime.out', 'w') as fout:
    for i in range(len(finalans)):
        print(finalans[i])
        print(finalans[i], file=fout)