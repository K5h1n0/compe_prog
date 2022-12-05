import copy
n = int(input())
l = list(map(int, input().split()))
l2 = copy.copy(l) 
l2.sort()
print(l.index(l2[-2])+1)