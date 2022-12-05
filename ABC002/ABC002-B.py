s = input()
ans = ""
for i in range(len(s)):
    if s[i] == "a" or s[i] == "i" or s[i] == "u" or s[i] == "e" or s[i] == "o":
        pass
    else:
        ans += s[i]
print(ans)