s = list(input())
s.sort()
ans = 0
for i in s:
    if i == "1":
        ans += 1
print(ans)