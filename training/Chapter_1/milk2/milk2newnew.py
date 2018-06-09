"""
ID: warreng1
LANG: PYTHON3
TASK: milk2
"""
with open('milk2.in', 'r') as fin:
    num = int(fin.readline())
    time = []
    for t in range(num):
        time.append(list(map(int, fin.readline().split())))
time.sort()
idle = [0]
newpair = False
for i in range(len(time)):
    if i == 0:
        prestart = time[i][0]
        prestop = time[i][1]
        consec = [prestop-prestart]
        continue
    start = time[i][0]
    stop = time[i][1]
    if start >= prestart and start <= prestop and stop > prestop:
        prestop = stop
        continue
    elif stop <= prestop and start >= prestart:
        continue
    elif start > prestop:
        idle.append(start-prestop)
        consec.append(prestop-prestart)
        prestart = start
        prestop = stop
print(max(consec), max(idle))
with open('milk2.out', 'w') as fout:
    print(max(consec), max(idle), file=fout)