"""
ID: warreng1
LANG: PYTHON3
TASK: beads
"""
l = []
val = []
wcount = 0
con = False
with open('beads.in', 'r') as file:
    number = int(file.readline())
    line = file.readline()
    line = line.rstrip('\n')

file2 = open('beads.out', 'w')

#Reference: ord('b') = 98, ord('r') = 114, ord('w') = 119

for x in range(len(line)):
    l.append(line[x])
for x, y in zip(l, range(len(l))):
    if x == 'w':
        wcount += 1
        if val == []:
            val.append(y)
            val.append(y)
        elif val != []:
            del val[-1]
            val.append(y)
    elif x == 'r' and y == 0:
        
        if l[1] == 'w':
            con = True

    elif x == 'b' and y == 0:
        
        if l[1] == 'w':
            con = True
    
    elif x == 'b':
        if wcount > 0:
            wcount = 0
            if l[y-1] and l[y-2] and l[y-3] and l[y-4] == 'r':
                for x in range(val[0], val[1]+1):
                    l[x] = 'r'
            else:
                for x in range(val[0], val[1]+1):
                    l[x] = 'b'
        val = []

    elif x == 'r':
        if wcount > 0:
            wcount = 0
            if l[y-1] == 'b' and l[y-2] == 'b' and l[y-3] == 'b'and l[y-4] == 'b':
                for x in range(val[0], val[1]+1):
                    l[x] = 'b'
            else:
                for x in range(val[0], val[1]+1):
                    l[x] = 'r'
        val = []
if wcount > 0:
    let = l[val[0]-1]
    for x in range(val[0], val[1]+1):
        l[x] = let
if con == True:
    l[1] = l[0]
y = 0
for x in l:
    if x == 'w':
        y += 1
    if y == len(l):
        for x in range(len(l)):
            l[x] = 'r'
val = []
for x in range(len(l)):
    if val == []:
        val.append([x, x])
    elif l[x] == l[x-1]:
        val[-1][1] = x
    else:
        val.append([x, x])
val2 = []
for x in range(len(val)):
    val2.append((int(val[x][1]) - int(val[x][0]))+1)
val = []
if len(val2) == 1:
    val = val2
else:
    for x in range(len(val2)):
        try:
            val.append(val2[x]+val2[x+1])
        except:
            if l[-1] == l[0]:
                smalllist = [val2[x-1]]
                smalllist.append(val2[1])
                val.append(max(smalllist)+val2[x]+val2[0])
            else:
                val.append(val2[x]+val2[0])
print(max(val), file=file2)
#print(max(val), '\n', val, '\n\n\n', val2, '\n\n', l)
file2.close()
