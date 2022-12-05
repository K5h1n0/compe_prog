import copy
n = int(input())
l = list(map(int,input().split()))
l2 = copy.copy(l)
l2 = list(set(l2))
if len(l) == len(l2):
    print("YES")
else:
    print("NO")