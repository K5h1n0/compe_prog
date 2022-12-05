import math
n,d = map(int,input().split())
l = []
for i in range(n):
    l.append(list(map(int,input().split())))
l2 = []
for i in range(n-1):
    for j in range(i+1,n):
        summary = 0
        for k in range(d):
            summary += abs(l[i][k]-l[j][k])**2
        l2.append(math.sqrt(summary))
cnt = 0
for i in range(len(l2)):
    if l2[i]%1 == 0:
        cnt += 1
print(cnt)