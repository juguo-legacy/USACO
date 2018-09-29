def recursion(potato, amount, taco):
    if amount == 0:
        return taco
    else:
        potatotaco = recursion(potato, amount-1, taco)
        listpotatotaco = list(potatotaco)
        newpotatotaco = []
        for i in range(len(listpotatotaco)//2):
            newpotatotaco.append(listpotatotaco[i])
        newpotatotaco = newpotatotaco+list(potato)
        newpotatotaco = newpotatotaco+listpotatotaco[len(listpotatotaco)//2:len(listpotatotaco)]
        returntaco = ''.join(newpotatotaco)
        return returntaco
potatotaco = recursion('potato', 2, 'taco')
print(potatotaco)