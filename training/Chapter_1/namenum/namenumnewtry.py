"""
ID: warreng1
LANG: PYTHON3
TASK: namenum
"""
with open('namenum.in', 'r') as fin:
    num = int(fin.readline())
    numbertoletter = {'2' : ['A', 'B', 'C'], '3' : ['D', 'E', 'F'], '4' : ['G', 'H', 'I'], '5' : ['J', 'K', 'L'], '6' : ['M', 'N', 'O'], '7' : ['P', 'R', 'S'], '8' : ['T', 'U', 'V'], '9' : ['W', 'X', 'Y']}

with open('dict.txt', 'r') as fin1:
    names = {i.rstrip() for i in fin1}

class TriTree:
    def __init__(self, data):
        self.data = data
        self.first = None
        self.second = None
        self.third = None
    def setFirst(self, child):
        self.first = child
        return child
    def setSecond(self, child):
        self.second = child
        return child
    def setThird(self, child):
        self.third = child
        return child
    
def buildTree(num):
    root = TriTree('')
    curTreeNodes = [root]  

    for n in num:
        chars = numbertoletter[n]
        tempTreeNodes = []
        for node in curTreeNodes:
            tempTreeNodes.append(node.setFirst(TriTree(chars[0])))
            tempTreeNodes.append(node.setSecond(TriTree(chars[1])))
            tempTreeNodes.append(node.setThird(TriTree(chars[2])))
        curTreeNodes = tempTreeNodes
    return root

result = set()

def readTree(tree, name):
    if tree.first == None:
        result.add(name+tree.data)
    else:
        readTree(tree.first, name+tree.data)
        readTree(tree.second, name+tree.data)
        readTree(tree.third, name+tree.data)

tree = buildTree(str(num))
readTree(tree, '')
finallist = sorted(list(result&names))
with open('namenum.out', 'w') as fout:
    for i in finallist:
        print(i)
        print(i, file=fout)
    if finallist == []:
        print("NONE")
        print("NONE", file=fout)