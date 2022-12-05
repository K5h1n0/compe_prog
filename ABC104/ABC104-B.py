s = input()
Ccnt = 0
ans = "AC"
if s[0] == "A":
    s = s[1:]
    for i in range(len(s)):
        if (1 <= i and i <= len(s)-2) and s[i] == "C":
            Ccnt += 1
        elif ord(s[i]) < 97 or 122 < ord(s[i]):
            ans = "WA"
    if Ccnt != 1:
        ans = "WA"
else:
    ans = "WA"
print(ans)