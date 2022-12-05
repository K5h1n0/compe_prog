import itertools
l = []
for i in range(3):
    l.append(list(map(int,input().split())))
l = list(itertools.chain.from_iterable(l))
n = int(input())
for i in range(n):
    a = int(input())
    if a in l:
        l[l.index(a)] = -1
if l[0] == l [1] == l[2] or l[3] == l [4] == l[5] or l[6] == l [7] == l[8] or l[0] == l [3] == l[6] or l[1] == l [4] == l[7] or l[2] == l [5] == l[8] or l[0] == l [4] == l[8] or l[2] == l [4] == l[6]:
    print("Yes")
else:
    print("No")