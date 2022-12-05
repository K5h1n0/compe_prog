from copy import copy

n = int(input())
l = list(map(int,input().split()))
l2 = copy(l)
l2 = list(set(l))
l2.sort()
l3 = [0]*n
for i in range(n):
    for j in range(len(l)):
        if i ==len(l2[l2.index(l[j])+1:]):
            l3[i] += 1
for i in l3:
    print(i)