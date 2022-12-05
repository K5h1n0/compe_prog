s = input()
t = input()
ans = "No"
for i in range(len(s)):
    s = s[1:] + s[0]
    if t == s:
        ans = "Yes"
print(ans)