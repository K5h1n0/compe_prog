s = input()
ans = "Yes"
for i in range(len(s)):
    if i%2 == 0 and (s[i] == "R" or s[i] == "U" or s[i] == "D"):
        pass
    elif i%2 == 1 and (s[i] == "L" or s[i] == "U" or s[i] == "D"):
        pass
    else:
        ans = "No"
print(ans)