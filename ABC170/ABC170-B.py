x,y = map(int,input().split())
ans = "No"
for i in range(x+1):
    if (i * 4) + ((x-i) *2) == y:
        ans = "Yes"
print(ans)