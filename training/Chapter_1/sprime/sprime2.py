"""
ID: warreng1
LANG: PYTHON3
TASK: sprime
"""
with open('sprime.in', 'r') as fin:
    N = int(fin.readline())
import math
basicprimes = [1, 3, 7, 9]
onebasicprimes = [2, 3, 5, 7]
def maketestprimes(primes):
    if len(primes) == 1:
        return primes[0]
    else:
        curprime = primes[0]
        nextprime = maketestprimes(primes[1:])
        retprime = []
        for i in curprime:
            for j in nextprime:
                retprime.append(int(str(i)+str(j)))
        return retprime
            

if N != 1:
    for i in range(N-1):
        onebasicprimes = maketestprimes([onebasicprimes]+[basicprimes])
        editprimes = onebasicprimes[:]
        for i in onebasicprimes:
            ending = int(math.sqrt(i))
            if ending % 2 == 0:
                ending += 1
            for j in range(3, ending+1, 2):
                if i%j == 0:
                    editprimes.remove(i)
                    break
        onebasicprimes = editprimes
    finalans = onebasicprimes
else:
    finalans = [2, 3, 5, 7]
with open('sprime.out', 'w') as fout:
    for i in finalans:
        print(i, file=fout)