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
def makePhrases(lists):
    if len(lists) == 1:
        return lists[0]
    else:
        firstEle = lists[0]
        lastStep = makePhrases(lists[1:])
        ret = []
        for c in firstEle:
            for i in lastStep:
                if c not in i:
                    ret.append(c+i)
        return ret

def MakePairsForSet(lists):
    returnl = []
    amountofpairs = N//2
    for i in lists:
        pairl = []
        for k in range(1, amountofpairs+1):
            pairl.append(tuple(sorted(list(i[(k-1)*2:k*2]))))
        returnl.append(tuple(sorted(pairl)))
    return set(sorted(returnl))

# Make DISTINCT pairs
distinctPairs = []
makePhrasesinput= [[str(i) for i in range(N)]]*N

AllPairs = MakePairsForSet(makePhrases(makePhrasesinput))
print('here now')
pairing = []
# Start checking, start by making a NEXTMOVE LIST
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
# Check
origins = list(range(N))
ansloops = 0
breakthrough = False
for i in AllPairs:
    newpair = []
    for j in i:
        for k in j:
            newpair.append(int(k))
    appendpair = [None]*len(newpair)
    for x in range(len(newpair)):
        if x % 2 == 1:
            appendpair[newpair[x]] = newpair[x-1]
            appendpair[newpair[x-1]] = newpair[x]
    for origin in origins:
        newcoords = origin
        add = 0
        while add == 0:
            nextplace = NextMove[newcoords]
            if nextplace == None:
                break
            else:
                newcoords = appendpair[nextplace]
            if newcoords == origin:
                breakthrough = True
                add = 1
        ansloops += add
        if breakthrough == True:
            breakthrough = False
            break
with open('wormhole.out', 'w') as fout:
    print(ansloops, file=fout)