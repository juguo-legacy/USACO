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

possiblewords = ['' for i in range(3**len(str(num)))]
divider = 1
lengthofpos = 3**len(str(num))

for i in range(len(str(num))):
    y = 0
    divider *= 3
    for t in range(int(divider/3)):
        for j in numbertoletter[int(str(num)[i])]:
            for k in range(y, int(lengthofpos/divider)+y):
                possiblewords[k] += j
            y += int(lengthofpos/divider)

ans = list(set(possiblewords)&names)
ans.sort()
if ans == []:
    ans = ['NONE']
with open('namenum.out', 'w') as fout:
    for i in ans:
        print(i)
        print(i, file=fout)