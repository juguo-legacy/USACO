"""
ID: warreng1
LANG: PYTHON3
TASK: milk
"""
with open('milk.in', 'r') as fin:
    neededmilk, farmers = fin.readline().split()
    neededmilk = int(neededmilk)
    farmers = int(farmers)
    deals = []
    for _ in range(farmers):
        deals.append(list(map(int, fin.readline().split())))
    deals.sort()

currentmilk = 0
centsused = 0

for i in range(len(deals)):
    if currentmilk + deals[i][1] > neededmilk:
        milkleft = neededmilk-currentmilk
        centsused += deals[i][0]*milkleft
        break
    centsused += deals[i][0]*deals[i][1]
    currentmilk += deals[i][1]

with open('milk.out', 'w') as fout:
    print(centsused)
    print(centsused, file=fout)