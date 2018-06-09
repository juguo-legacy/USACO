"""
ID: warreng1
LANG: PYTHON3
TASK: friday
"""

file = open('friday.in', 'r')
file2 = open('friday.out', 'w')

currentyear = 1900
months = {"January" : 31, "Febuary" : 28, "March" : 31, "April" : 30, \
          "May" : 31, "June" : 30, "July" : 31, "August" : 31, \
          "September" : 30, "October" : 31, "November" : 30, "December" : 31}
days = {"Monday" : 0, "Tuesday" : 0, "Wenesday" : 0, "Thursday" : 0,\
        "Friday" : 0, "Saturday" : 0, "Sunday" : 0}

for x in file:
    x = x.rstrip('\n')
    number = int(x)
monthdays = 0
day = 13
leapyear = False
yearafter = False
applyamount = 0
for x in range(number):
    if currentyear % 100 == 0:
        if currentyear % 400 == 0:
            months['Febuary'] = 29
            leapyear = True
    elif currentyear % 4 == 0:
        months['Febuary'] = 29
        leapyear = True
    for z in range(12):
        y = z+1
        day += monthdays
        day1 = day % 7
        if yearafter == True:
            day1 += 1
            day1 = day1 % 7
        if day1 == 1:
            days['Monday'] += 1
        elif day1 == 2:
            days['Tuesday'] += 1
        elif day1 == 3:
            days['Wenesday'] += 1
        elif day1 == 4:
            days['Thursday'] += 1
        elif day1 == 5:
            days['Friday'] += 1
        elif day1 == 6:
            days['Saturday'] += 1
        elif day1 == 0:
            days['Sunday'] += 1
        if y == 1:
            monthdays = months['January']
        elif y == 2:
            monthdays = months['Febuary']
        elif y == 3:
            monthdays = months['March']
        elif y == 4:
            monthdays = months['April']
        elif y == 5:
            monthdays = months['May']
        elif y == 6:
            monthdays = months['June']
        elif y == 7:
            monthdays = months['July']
        elif y == 8:
            monthdays = months['August']
        elif y == 9:
            monthdays = months['September']
        elif y == 10:
            monthdays = months['October']
        elif y == 11:
            monthdays = months['November']
        elif y == 12:
            monthdays = months['December']
    months['Febuary'] = 28
    currentyear += 1
print(days['Saturday'], days['Sunday'], days['Monday'], days['Tuesday'],\
      days['Wenesday'], days['Thursday'], days['Friday'], file=file2)
file2.close()