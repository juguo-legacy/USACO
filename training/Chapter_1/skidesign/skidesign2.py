"""
ID: warreng1
LANG: PYTHON3
TASK: skidesign
"""
with open('skidesign.in', 'r') as fin:
    N = int(fin.readline())
    hills = sorted(list(map(int, [fin.readline().rstrip() for i in range(N)])))

def calculateamount(hills, hillrange):
    moneyneeded = 0
    for i in hills:
        if i > hillrange[1]:
            moneyneeded += (i-hillrange[1])**2
        elif i < hillrange[0]:
            moneyneeded += (hillrange[0]-i)**2
    return moneyneeded

startpoint = 0
endpoint = 17
moneys = []
while True:
    startpoint += 1
    endpoint += 1
    moneys.append(calculateamount(hills, [startpoint, endpoint]))
    if len(moneys) != 0:
        if moneys[len(moneys)-1] > moneys[len(moneys)-2]:
            break
with open('skidesign.out', 'w') as fout:
    print(moneys[-2], file=fout)