#解説AC

import math

n,k = map(int,input().split())
a = set(map(int,input().split()))
l = []
l_torch = []
for i in range(n+1):
    if i == 0:
        l.append([])
    else:
        tmp = list(map(int,input().split()))
        if i in a:
            l_torch.append(tmp)
        else:
            l.append(tmp)
# print(a)
# print(l)
# print(l_torch)
ans = []
for i in range(1,len(l)):
    minimum = 99999999999999
    for j in range(len(l_torch)):
        kyori = math.sqrt((l[i][0] - l_torch[j][0])**2 + (l[i][1] - l_torch[j][1])**2)
        if minimum > kyori:
            minimum = kyori
    ans.append(minimum)
print(max(ans))