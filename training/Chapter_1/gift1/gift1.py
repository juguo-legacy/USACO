"""
ID: warreng1
LANG: PYTHON3
TASK: gift1
"""

file = open('gift1.in', 'r')
file2 = open('gift1.out', 'w')
y = 0
names = {}
names1 = []
subto = 0
iftrue = False

for x in file:
    number = int(x)
    break

for x in file:
    x = x.rstrip('\n')
    names[x] = 0
    names1.append(x)
    y += 1
    if y == number:
        break
while True:
    for x in file:
        x = x.rstrip("\n")
        name = x
        break
    for x in file:
        x = x.rstrip("\n")
        num1, num2 = x.split()
        try:
            if int(num1) % int(num2) != 0:
                subto = int(num1) % int(num2)
        except ZeroDivisionError:
            subto = 0
        try:
            answer = int(int(num1) / int(num2))
        except ZeroDivisionError:
            answer = 0
            iftrue = True
        num1 = int(num1) - subto
        subto = 0
        names[name] -= num1
        num2 = int(num2)
        break
    else:
        break
    if iftrue == False:
        for x in file:
            x = x.rstrip("\n")
            names[x] += answer
            num2 -= 1
            if num2 <= 0:
                break
    else:
        iftrue = False

for x in range(len(names1)):
    print(names1[x],names[names1[x]], file=file2)
file2.close()
