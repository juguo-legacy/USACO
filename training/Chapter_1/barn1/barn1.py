"""
ID: warreng1
LANG: PYTHON3
TASK: barn1
"""
with open('barn1.in', 'r') as fin:
    boards, stalls, numcows = fin.readline().split()
    boards = int(boards)
    stalls = int(stalls)
    numcows = int(numcows)
    if boards > numcows:
        boards = numcows
    stalloccupied = []
    for _ in range(numcows):
        stalloccupied.append(int(fin.readline()))
stalloccupied.sort()

#Find Gaps
gaps = [stalloccupied[i]-stalloccupied[i-1] for i in range(1, len(stalloccupied))]
sortgaps = sorted(gaps, reverse=True)
# Divide "stalloccupied"
biggestnums = [sortgaps[i] for i in range(boards-1)]

divides = []
session = []

for i in range(len(stalloccupied)):
    session.append(stalloccupied[i])
    if i == len(stalloccupied)-1:
        session.append(str(session[-1]-session[0]+1))
        divides.append(session)
    elif gaps[i] in biggestnums:
        biggestnums.remove(gaps[i])
        session.append(str(session[-1]-session[0]+1))
        divides.append(session)
        session = []
        continue
# Divides works like this, numbers of the divides, and the total amount blocked as a str
finalans = [int(divides[i][-1]) for i in range(len(divides))]

#Output
with open('barn1.out', 'w') as fout:
    print(sum(finalans))
    print(sum(finalans), file=fout)