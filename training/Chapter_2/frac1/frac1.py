"""
ID: warreng1
LANG: PYTHON3
TASK: frac1
"""
import fractions
with open('frac1.in', 'r') as fin:
    N = int(fin.readline())
genall = {(0, 1), (1, 1)}
for denominator in range(1, N+1):
    for numerator in range(1, denominator):
        frac = (numerator, denominator)
        if frac in genall:
            continue
        genall.add(frac)
genall = sorted(list(set([fractions.Fraction(i[0], i[1]).limit_denominator() for i in list(genall)])))
with open('frac1.out', 'w') as fout:
    for i in genall:
        if i == 0:
            print('0/1', file=fout)
        elif i == 1:
            print('1/1', file=fout)
        else:
            print(i, file=fout)