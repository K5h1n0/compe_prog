n = int(input())
a,p,x = [0]*n,[0]*n,[0]*n
l = []
for i in range(n):
    a[i],p[i],x[i] = map(int, input().split())
    l.append(x[i]-a[i])
min = 9999999999
for i in range(n):
    if l[i] > 0 and min > p[i]:
        min = p[i]
if min == 9999999999:
    print(-1)
else:
    print(min)