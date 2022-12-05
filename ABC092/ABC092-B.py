n = int(input())
d,x = map(int,input().split())
l = []
for i in range(n):
    l.append(int(input()))
ans = 0
for i in range(len(l)):
    if d%l[i] > 0:
        ans += d // l[i] + 1
    else:
        ans +=  d // l[i]
ans += x
print(ans)