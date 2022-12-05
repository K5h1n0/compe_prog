n,x = map(int, input().split())
a = list(map(int, input().split()))
l = []
for i in range(n):
    if a[i] != x:
        l.append(a[i])
print(*l)