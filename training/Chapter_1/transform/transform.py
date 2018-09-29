"""
ID: warreng1
LANG: PYTHON3
TASK: transform
"""
with open('transform.in', 'r') as fin:
    size = int(fin.readline())
    originalraw = [fin.readline().rstrip() for x in range(size)]
    newraw = [fin.readline().rstrip() for x in range(size)]
    original = [[y for y in x] for x in originalraw]
    new = [[y for y in x] for x in newraw]

def rotate90(l, size):
    returnl = [x[:] for x in l]
    for i in range(size):
        for j in range(size):
            returnl[i][j] = l[size - j - 1][i]
    return returnl

def flip(l, size):
    returnl = [x[:] for x in l]
    for i in range(size):
        for j in range(size):
            returnl[i][j] = l[i][size - j - 1]
    return returnl

choiceone = rotate90(original, size)
choicetwo = rotate90(choiceone, size)
choicethree = rotate90(choicetwo, size)
choicefour = flip(original, size)
choicefivea = rotate90(flip(original, size), size)
choicefiveb = rotate90(choicefivea, size)
choicefivec = rotate90(choicefiveb, size)
choicesix = original
#None for choice seven, it is an else statement.

#Looking for matching list
if new == choiceone:
    finalanswer = 1
elif new == choicetwo:
    finalanswer = 2
elif new == choicethree:
    finalanswer = 3
elif new == choicefour:
    finalanswer = 4
elif new == choicefivea:
    finalanswer = 5
elif new == choicefiveb:
    finalanswer = 5
elif new == choicefivec:
    finalanswer = 5
elif new == choicesix:
    finalanswer = 6
else:
    finalanswer = 7

print(finalanswer)
with open('transform.out', 'w') as fout:
    print(finalanswer, file=fout)