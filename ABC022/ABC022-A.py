n,s,t=map(int,input().split())
ans = 0
a = int(input())
if s <= a and a <= t:
    ans += 1
for i in range(n-1):
    tmp = int(input())
    a += tmp
    if s <= a and a <= t:
        ans += 1
print(ans)