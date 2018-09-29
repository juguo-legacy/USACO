"""
ID: warreng1
LANG: PYTHON3
TASK: namenum
"""
import itertools
with open('namenum.in', 'r') as fin:
    num = int(fin.readline())
    numbertoletter = {2 : ['A', 'B', 'C'], 3 : ['D', 'E', 'F'], 4 : ['G', 'H', 'I'], 5 : ['J', 'K', 'L'], 6 : ['M', 'N', 'O'], 7 : ['P', 'R', 'S'], 8 : ['T', 'U', 'V'], 9 : ['W', 'X', 'Y']}

with open('dict.txt', 'r') as fin1:
    names = {i.rstrip() for i in fin1}

possibiles = set()
lists = [numbertoletter[int(i)] for i in str(num)]

possibiles = set(''.join(i) for i in (itertools.product(*lists)))

incommon = sorted(list(possibiles&names))

with open('namenum.out', 'w') as fout:
    for i in incommon:
        print(i)
        print(i, file=fout)
    if incommon == []:
        print("NONE")
        print("NONE", file=fout)