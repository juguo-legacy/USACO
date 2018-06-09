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
time.sort(key=lambda x: x[1])
consecutive = [x[1]-x[0] for x in time]
consec = 0
for i in range(1, len(time)):
    if time[i-1][1] >= time[i][0] and consec != 0:
        consecutive.append(time[i][1]-time[i-1][0])
        consecutive.append(time[i][1]-time[(i-1)-consec][0])
        consec += 1
    elif time[i-1][1] >= time[i][0]:
        consecutive.append(time[i][1]-time[i-1][0])
        consec += 1
idle = [0]
impossible = []
for x in range(1, len(time)):
    if time[x][0] < time[x-1][1]:
        impossible.append(time[x])
possible = False
for x in range(len(time)-1):
    if impossible == []:
        if (time[x][1] < time[x+1][0]):
            idle.append(time[x+1][0]-time[x][1])
            continue
    for y in impossible:
        if (time[x][1] < time[x+1][0]):
            if time[x+1][0] < y[0] or time[x+1][0] > y[1]:
                possible = True
            else:
                possible = False
                break
    if possible == True:
        idle.append(time[x+1][0]-time[x][1])
print(consecutive)
print('%d_%d' % (max(consecutive), max(idle)))
with open('milk2.out', 'w') as fout:
    print('%d %d' % (max(consecutive), max(idle)), file=fout)