#解説AC
n,w = map(int,input().split())
l = []
for i in range(n):
    a,b = map(int,input().split())
    l.append([a,b])
l.sort(reverse=True)
ans = 0
for i in range(n):
    ans += l[i][0] * min(w,l[i][1])
    w -= l[i][1]
    if w < 0:
        break
print(ans)