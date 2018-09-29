N = 4
makePhrasesinput= [[str(i) for i in range(N)]]*N
count = 10
def makePhrases(lists):
    global count
    count -= 1
    print("count=", count)
    print("len lists", len(lists))
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
        newret = []
        if len(ret) % 2 == 0:
            for k in range(0, len(ret)):
                for i in range(0, len(ret[k]), 2):
                    addl = []
                    addl.append(sorted([int(ret[k][i]), int(ret[k][i+1])]))
        return ret
def getans(lists, i):
    nextI = None
    for k in range(i, len(lists)):
        if lists[k] == None:
            nextI = k
            break
    if nextI == None or i == len(lists):
        print(lists)
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