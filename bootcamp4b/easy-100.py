n = int(input())
l = list(map(int,input().split()))
l = [0] + l
ans = 0
for i in range(1,len(l)):
    if i == l[l[i]]:
        ans += 1
print(ans//2)