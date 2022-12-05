n = int(input())
l = [input() for _ in range(n)]
ans = "No"
for i in range(n-1):
    for j in range(i+1,n):
        if l[i] == l[j]:
            ans = "Yes"
print(ans)