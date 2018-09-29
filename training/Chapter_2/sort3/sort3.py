"""
ID: warreng1
LANG: PYTHON3
TASK: sort3
"""
with open('sort3.in', 'r') as fin:
    N = fin.readline()
    changelist = [int(fin.readline()) for _ in range(N)]
print(changelist)