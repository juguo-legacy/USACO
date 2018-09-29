"""
ID: warreng1
LANG: PYTHON3
TASK: sprime
"""
with open('sprime.in', 'r') as fin:
    N = int(fin.readline())
import math
start = 9
end =  10**N
def findprimes(start, end):
    returnl = [2, 3, 5, 7]
    for i in range(start, end, 2):
        ending = int(math.sqrt(int(i)))
        if ending % 2 == 0:
            ending += 1
        for j in range(3, ending+1, 2):
            if int(i)%j == 0:
                break
            elif j == ending:
                returnl.append(int(i))
    return returnl
def primeprimes(start, end):
    returnl = [2, 3, 5, 7]
    for i in range(start, end, 2):
        isprime = True
        for j in returnl:
            if i%j == 0:
                isprime = False
                break
        if isprime:
            returnl.append(i)
    return returnl
primeslist = primeprimes(start, end)
print(len(primeslist))