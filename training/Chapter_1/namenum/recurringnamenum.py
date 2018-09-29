"""
ID: warreng1
LANG: PYTHON3
TASK: namenum
"""
with open('namenum.in', 'r') as fin:
    num = int(fin.readline())
    numbertoletter = {2 : ['A', 'B', 'C'], 3 : ['D', 'E', 'F'], 4 : ['G', 'H', 'I'], 5 : ['J', 'K', 'L'], 6 : ['M', 'N', 'O'], 7 : ['P', 'R', 'S'], 8 : ['T', 'U', 'V'], 9 : ['W', 'X', 'Y']}

with open('dict.txt', 'r') as fin1:
    names = {i.rstrip() for i in fin1}

lists = [numbertoletter[int(i)] for i in str(num)]

def makePhrases(lists):
    if len(lists) == 1:
        return lists[0]
    else:
        firstEle = lists[0]
        lastStep = makePhrases(lists[1:])
        ret = []
        for c in firstEle:
            for i in lastStep:
                ret.append(c+i)
        return ret

similar = set(makePhrases(lists))&names
sortans = sorted(list(similar))

with open('namenum.out', 'w') as fout:
    if sortans == []:
        print('NONE', file=fout)
    else:
        for i in sortans:
            print(i)
            print(i, file=fout)