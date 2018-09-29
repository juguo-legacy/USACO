"""
ID: warreng1
LANG: PYTHON3
TASK: palsquare
"""

with open('palsquare.in') as fin:
    base = int(fin.readline())

def converttobase(num, base):
    newstr = ''
    copynum = num
    while copynum:
        mod = copynum % base
        copynum = copynum // base
        newstr = chr(48+mod+7*(mod>=10)) + newstr
    return newstr

palindromes = []

for i in range(1, 301):
    result = converttobase(i*i, base)
    converti = converttobase(i, base)
    if result == result[::-1]:
        palindromes.append([converti, result])

with open('palsquare.out', 'w') as fout:
    for i in range(len(palindromes)):
        #print(palindromes[i][0], palindromes[i][1])
        print(palindromes[i][0], palindromes[i][1], file=fout)