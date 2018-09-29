"""
ID: warreng1
LANG: PYTHON3
TASK: milk3
"""
with open('milk3.in', 'r') as fin:
    ABC = list(map(int, fin.readline().split()))
ABCval = [0, 0, ABC[2]]

def givemilk(giver, receiver, ABCval):
    vari = ABC[receiver]-ABCval[receiver]
    if ABCval[giver]-vari < 0:
        vari -= vari-ABCval[giver]
    ABCval[receiver] += vari
    ABCval[giver] -= vari
    return ABCval

finalans = []
exsisting = [ABCval[:]]

def testmilk(exsisting, ABC, ABCval, finalans, count):
    copyABCval = ABCval[:]
    copycopyABCval = ABCval[:]
    possibles = []
    for i in range(len(copycopyABCval)):
        if count != 0:
            for p in range(len(copyABCval)):
                for k in range(len(copyABCval)):
                    if copyABCval[p] > 0 and copyABCval[k] != ABC[k] and k != p:
                        possibles.append([k, 'receive', p])
        else:
            for k in range(len(copyABCval)):
                if copyABCval[k] > 0 and copyABCval[i] != ABC[i] and k != i:
                    possibles.append([k, 'give', i])
        counter = 0
        for j in range(len(possibles)):
            ABCval2 = ABCval[:]
            if possibles[j][1] == 'give':
                copyABCval = givemilk(possibles[j][0], possibles[j][2], ABCval2)
            else:
                copyABCval = givemilk(possibles[j][2], possibles[j][0], ABCval2)
            if copyABCval in exsisting:
                counter += 1
                continue
            exsisting.append(copyABCval[:])
            testmilk(exsisting, ABC, copyABCval, finalans, count+1)
            if count != 0:
                counter += 1
        if counter == len(possibles):
            count -= 1
            return
        for y in exsisting:
            if y[0] == 0:
                finalans.append(y[2])
        exsisting = [copycopyABCval[:]]
        copyABCval = copycopyABCval[:]
        possibles = []
count = 0
testmilk(exsisting, ABC, ABCval, finalans, count)
finalans = sorted(list(set(finalans)))
finalstr = ' '.join([str(i) for i in finalans])
with open('milk3.out', 'w') as fout:
    print(finalstr, file=fout)