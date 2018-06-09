'''
ID: warreng1
LANG: PYTHON3
TASK: gift1

'''
order = []

with open('gift1.in') as fin: 
    num = int(fin.readline())
    for _ in range(num):
        order.append(fin.readline().rstrip())
    rawtransactions = fin.readlines()
transactions = []
names = {i: 0 for i in order}
for i in range(len(rawtransactions)):
    if rawtransactions[i].rstrip() in names:
        transactions.append(rawtransactions[i].rstrip())
    else:
        transactions.append(list(map(int, rawtransactions[i].rstrip().split())))
givemoney = False
for i in range(len(transactions)):
    if type(transactions[i]) is list:
        if transactions[i][1] != 0:
            amounttoadd = int(transactions[i][0]/transactions[i][1])
            amounttoaddback = transactions[i][0]%transactions[i][1]
        else:
            amounttoadd = 0
            amounttoaddback = 0
        names[name] -= transactions[i][0]-amounttoaddback
        looping = transactions[i][1]
        if looping != 0:
            givemoney = True
        continue
    elif givemoney == False:
        name = transactions[i]
        continue
    elif givemoney == True:
        names[transactions[i]] += amounttoadd 
        looping -= 1
        if looping == 0:
            givemoney = False
with open('gift1.out', 'w') as fout:
    for i in order:
        print('%s %d' % (i, names[i]))
        print('%s %d' % (i, names[i]), file=fout)