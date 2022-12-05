n,t = map(int,input().split())
l = []
for i in range(n):
    l.append(int(input()))
ans = 0
for i in range(1,len(l)):
    tmp = l[i]-l[i-1]
    if tmp > t:
        ans += t
    else:
        ans += tmp
ans += t
print(ans)