s = input()
t = input()
ans = "Yes"
for i in range(len(s)):
    if len(t) <= i:
        ans = "No"
        break
    if s[i] != t[i]:
        ans = "No"
print(ans)