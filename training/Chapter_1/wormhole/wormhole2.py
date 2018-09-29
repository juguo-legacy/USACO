"""
ID: warreng1
LANG: PYTHON3
TASK: wormhole
"""
with open('wormhole.in', 'r') as fin:
    N = int(fin.readline())
    holes = [list(map(int, fin.readline().rstrip().split())) for i in range(N)]
holes.sort()
holes.sort(key=lambda x:x[1])
# Start by making a NextMove List
NextMove = []
for i in range(len(holes)):
    nextcheck = False
    newappend = "Not Ready"
    vals = []
    for j in range(len(holes)):
        if j < i:
            continue
        if holes[j][1] == holes[i][1] and holes[j][0] >= holes[i][0]:
            vals.append(j)
        try:
            if nextcheck == True:
                newappend = (vals[vals.index(i)+1])
            elif holes[j] == holes[i]:
                nextcheck = True
        except IndexError:
            newappend = None
        except ValueError:
            newappend = "Not Ready"
        if newappend == "Not Ready" and j == len(holes)-1:
            newappend = None
        if type(newappend) != str:
            break
    NextMove.append(newappend)
# Check Function
def check(lists):
    origins = list(range(N))
    ansloops = 0
    breakthrough = False
    for origin in origins:
        newcoords = origin
        add = 0
        while add == 0:
            nextplace = NextMove[newcoords]
            if nextplace == None:
                break
            else:
                newcoords = lists[nextplace]
            if newcoords == origin:
                breakthrough = True
                add = 1
        ansloops += add
        if breakthrough == True:
            breakthrough = False
            break
    return ansloops
finalans = 0
def getans(lists, i):
    nextI = None
    for k in range(i, len(lists)):
        if lists[k] == None:
            nextI = k
            break
    if nextI == None or i == len(lists):
        newadd = check(lists)
        global finalans
        finalans += newadd
        return

    for j in range(nextI, len(lists)):
        if j == nextI:
            continue
        else:
            if lists[j] == None:
                lists[nextI] = j
                lists[j] = nextI
                getans(lists, nextI + 1)
                lists[nextI] = None
                lists[j] = None
    return
test = getans([None]*N, 0)
with open('wormhole.out', 'w') as fout:
    print(finalans, file=fout)