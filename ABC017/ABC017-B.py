x = input()
i = 0
ans = "YES"
while i < len(x):
    if x[i] == "c" and x[i+1] == "h":
        i += 2
    elif x[i] == "o" or x[i] == "k" or x[i] == "u":
        i += 1
    else:
        ans = "NO"
        break
print(ans)