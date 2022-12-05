n,m = map(int, input().split())
l = list(map(int,input().split()))
sum = sum(l)
l.sort()
l.reverse()
ans = "Yes"
for i in range(m):
    if l[i] < sum/4/m:
        ans = "No"
print(ans)