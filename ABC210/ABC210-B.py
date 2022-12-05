n = int(input())
s = input()
s = list(s)
ans = ""
for i in range(len(s)):
    if s[i] == "1":
        if i % 2 ==0:
            ans = "Takahashi"
        else:
            ans = "Aoki"
        break
print(ans)