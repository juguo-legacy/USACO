"""
ID: warreng1
LANG: PYTHON3
TASK: beads
"""
with open('beads.in', 'r') as fin:
    lenbeads = int(fin.readline())
    beads = fin.readline()
beads = beads * 2
letterlist = list(beads)
def shrink(beadslist):
    curcounter = 1
    letter = beadslist[0]
    returnl = []
    countlist = []
    for i in range(1, len(beadslist)):
        if beadslist[i] == letter:
            curcounter += 1
        elif beadslist[i] != letter:
            countlist.append(curcounter)
            curcounter = 1
            returnl.append(letter)
            letter = beadslist[i]
        if i == len(beadslist)-1:
            countlist.append(curcounter)
            returnl.append(letter)
    return returnl, countlist

def combinee(shrinked, countlist):
    newl = []
    for i in range(len(shrinked)):
        for j in range(countlist[i]):
            newl.append(shrinked[i])
    return newl
        
# Make countlist and simplify letterlist:
shrinked, countlist = shrink(letterlist)
# Simplify shinkred
for i in range(1, len(shrinked)-1):
    if shrinked[i-1] == shrinked[i+1] and shrinked[i] == 'w':
        shrinked[i] = shrinked[i-1]
newl = combinee(shrinked, countlist)
# Shrink again
shrinked, countlist = shrink(newl)
#Preparation for the next step:
dupeshrinked = []
dupecount = []
# Put in w's
for i in range(len(shrinked)-1):
    dupeshrinked.append(shrinked[i])
    dupecount.append(countlist[i])
    if shrinked[i] != 'w' and shrinked[i+1] != 'w':
        dupeshrinked.append('w')
        dupecount.append(0)
dupeshrinked.append(shrinked[-1])
dupecount.append(countlist[-1])

# Combine w's with other remaining stuff(Step 6)

for i in range(len(dupeshrinked)):
    if dupeshrinked[i] == 'w' and dupecount[i] != 0:
        frontfour = []
        for j in range(1, 5):
            if i+j > len(dupeshrinked)-1:
                frontfour.append((i+j)-(len(dupeshrinked)-1))
            else:
                frontfour.append(i+j)
        if dupeshrinked[i-1]+dupeshrinked[i-2]+dupeshrinked[i-3]+dupeshrinked[i-4] >= dupeshrinked[frontfour[0]]+dupeshrinked[frontfour[1]]+dupeshrinked[frontfour[2]]+dupeshrinked[frontfour[3]]:
            dupecount[i-1] += dupecount[i]
            dupecount[i] = 0
        else:
            dupecount[i+1] += dupecount[i]
            dupecount[i] = 0

newl = combinee(dupeshrinked, dupecount)
shrinked, countlist = shrink(newl)
if len(shrinked) == 1:
    finalans = [countlist[0]]
elif shrinked[0] == shrinked[-1]:
    countlist[0] += countlist[-1]
    del shrinked[-1]
    del countlist[-1]
    finalans = []
else:
    finalans = []
if finalans == []:
    for i in range(len(countlist)):
        if i == 0:
            finalans.append(countlist[0]+countlist[-1])
            continue
        finalans.append(countlist[i]+countlist[i-1])
with open('beads.out', 'w') as fout:
    print(max(finalans))
    print(max(finalans), file=fout)