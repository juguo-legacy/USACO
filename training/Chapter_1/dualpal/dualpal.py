"""
ID: warreng1
LANG: PYTHON3
TASK: dualpal
"""

with open('dualpal.in', 'r') as fin:
    firstnumbers, start = fin.readline().split()
    firstnumbers = int(firstnumbers)
    start = int(start)

def converttobase(num, base):
    newstr = ''
    copynum = num
    while copynum:
        mod = copynum % base
        copynum = copynum // base
        newstr = chr(48+mod+7*(mod>=10)) + newstr
    return newstr

answers = []

while firstnumbers:
    #Look for matching numbers:
    amountofpalin = 0
    for i in range(2, 11):
        convertnum = converttobase(start+1, i)
        if convertnum == convertnum[::-1]:
            amountofpalin += 1
        if amountofpalin == 2:
            answers.append(start+1)
            firstnumbers -= 1
            break
    start += 1

with open('dualpal.out', 'w') as fout:
    for i in answers:
        #print(i)
        print(i, file=fout)