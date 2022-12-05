n = int(input())
l = []
l2 = []
for i in range(n):
    a = input()
    l.append(a)
    l2.append(a)
l2 = list(set(l2))
print("l2",l2)
l4 = [0]*len(l2)
print("l4",l4)
l3 = dict(zip(l2,l4))
print("l3",l3)
for i in l:
    if l3[i] == 0:
        print(i)
        l3[i] += 1
    else:
        s = i + "(" + str(l3[i]) + ")"
        print(s)
        l3[i]+=1
    



"""
from sys import stdin
input = stdin.readline
num,new2 =[],[]
new = set()
n = int(input().rstrip())
l = [input().rstrip() for _ in range(n)]
for i in l:
    if i not in new:
        new.add(i)
        new2.append(i)
        num.append(0)
        print(i)
    else:
        num[new2.index(i)] += 1
        print(i + "(" + str(num[new2.index(i)]) + ")")
"""
"""
from sys import stdin
input = stdin.readline
new,ans,num = [],[],[]
n = int(input().rstrip())
l = [input().rstrip() for _ in range(n)]
for i in range(n):
    if l[i] not in new:
        new.append(l[i])
        num.append(0)
        print(l[i])
    else:
        a = new.index(l[i])
        num[a] += 1
        moji =l[i] + "(" + str(num[a]) + ")"
        print(moji)
"""