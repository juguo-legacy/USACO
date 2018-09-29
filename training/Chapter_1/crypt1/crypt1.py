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
    '''
    if len(first) > 3 or len(second) > 3:
        return counter
    '''
    if set(first) <= set(strdigits):
        if set(second)<=set(strdigits):
            if set(str(int(firstnum)*int(secondnum)))<=set(strdigits):
                    counter += 1
    return counter

counter = 0
# Make and try Combinations
NotBigEnough = True
'''
Make a "five" digit number.  First two digits are the two digits on the bottom;
Last three digits are the three digits on the top.
'''
startnum = str(digits[0])*5
liststartnum = list(startnum)
combinations = [startnum]
onesDigitcount = 1
tensDigitCount = 1
hundredsCount = 1
TensCounts = 1
if N != 1:
    while NotBigEnough:
        if int(startnum[-1]) == digits[-1] and int(startnum[-2]) == digits[-1]:
            tempnum1 = list(startnum[:3]+str(digits[0])*2)
            tempnum1[-3] = str(digits[hundredsCount])
            tempnum1 = ''.join(tempnum1)

            tempnum2 = list(startnum[:3]+str(digits[0])*2)
            tempnum2[1] = str(digits[TensCounts])
            tempnum2 = ''.join(tempnum2)
            tensDigitCount = 1
            onesDigitcount = 1
            if int(tempnum1[-3:])*int(tempnum1[:2]) <= int(tempnum2[-3:])*int(tempnum2[:2]):
                liststartnum = list(tempnum1[:])
                hundredsCount += 1
            else:
                liststartnum = list(tempnum2[:])
                TensCounts += 1
                
        elif int(startnum[-1]) == digits[-1]:
            liststartnum[-1] = str(digits[0])
            liststartnum[-2] = str(digits[tensDigitCount])
            onesDigitcount = 1
            tensDigitCount += 1
        else:
            liststartnum[-1] = str(digits[onesDigitcount])
            onesDigitcount += 1
        
        startnum = ''.join(liststartnum)
        '''
        if len(str(int(startnum[-3:])*int(startnum[0]))) > 3 or len(str(int(startnum[-3:])*int(startnum[1]))) > 3:
            NotBigEnough = False
            '''
        if startnum == str(digits[-1])*5:
            NotBigEnough = False

        elif NotBigEnough:
            combinations.append(startnum)

print(combinations)

counter = 0
for i in combinations:
    counter = isTrue(i[-3:], i[:2], counter)

with open('crypt1.out', 'w') as fout:
    print(counter)
    print(counter, file=fout)