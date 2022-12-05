n,k = map(int,input().split())
s = list(input())
ans = ""
for i in range(n):
    if k-1 == i:
        ans += s[i].lower()
    else:
        ans += s[i]
print(ans)