s = input()
t = input()
atcoder = {"@","a","t","c","o","d","e","r"}
ans = "You can win"
for i in range(len(s)):
    if s[i] == "@" and t[i] in atcoder:
        pass
    elif t[i] == "@" and s[i] in atcoder:
        pass
    elif s[i] == t[i]:
        pass
    else:
        ans = "You will lose"
        break
print(ans)