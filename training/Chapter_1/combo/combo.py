"""
ID: warreng1
LANG: PYTHON3
TASK: combo
"""
with open('combo.in', 'r') as fin:
    N = int(fin.readline())
    fjCombo = list(map(int, fin.readline().split()))
    masterCombo = list(map(int, fin.readline().split()))
Nlist = list(range(1, N+1))

class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.middle = None

if N != 1:
    # Make a function that gets the numbers that are within the range of two.
    def get_two_near(num):
        num1 = num+1
        if num1 >= len(Nlist):
            num1 = num1-len(Nlist)
        newnum = num
        if newnum >= len(Nlist):
            newnum = newnum-len(Nlist)
        return [Nlist[num-3], Nlist[num-2], Nlist[num-1], Nlist[newnum], Nlist[num1]]

    def makecombos(tree, returnSet):
        for i in tree.left:
            for j in tree.middle:
                for k in tree.right:
                    returnSet.add(str(i)+str(j)+str(k))
        return returnSet

    fjComboPossibles = Tree()
    fjComboPossibles.left = sorted(get_two_near(fjCombo[0]))
    fjComboPossibles.middle = sorted(get_two_near(fjCombo[1]))
    fjComboPossibles.right = sorted(get_two_near(fjCombo[2]))

    masterComboPossibles = Tree()
    masterComboPossibles.left = sorted(get_two_near(masterCombo[0]))
    masterComboPossibles.middle = sorted(get_two_near(masterCombo[1]))
    masterComboPossibles.right = sorted(get_two_near(masterCombo[2]))

    returnSet = set()
    makecombos(fjComboPossibles, returnSet)
    makecombos(masterComboPossibles, returnSet)
else:
    returnSet = [1]

with open('combo.out', 'w') as fout:
    print(len(returnSet))
    print(len(returnSet), file=fout)