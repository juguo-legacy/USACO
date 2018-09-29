"""
ID: warreng1
LANG: PYTHON3
TASK: crypt1
"""
with open('crypt1.in', 'r') as fin:
    N = int(fin.readline())
    digits = sorted(list(map(int, fin.readline().split())))
    strdigits = [str(i) for i in digits]

def isTrue(firstnum, secondnum, counter):
    first = str(int(firstnum)*int(secondnum[1]))
    second = str(int(firstnum)*int(secondnum[0]))
    if len(first) > 3 or len(second) > 3:
        return counter
    if set(first) <= set(strdigits):
        if set(second)<=set(strdigits):
            if set(str(int(firstnum)*int(secondnum)))<=set(strdigits):
                if len(str(int(firstnum)*int(secondnum))) == 4:
                    counter += 1
    return counter

counter = 0
# Make and try Combinations

for a in digits:
    for b in digits:
        for c in digits:
            for d in digits:
                for e in digits:
                    abc = str(a*100+b*10+c)
                    de = str(d*10+e)
                    counter = isTrue(abc, de, counter)

with open('crypt1.out', 'w') as fout:
    print(counter)
    print(counter, file=fout)