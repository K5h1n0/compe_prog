s = input()
l = [0]*6
for i in range(len(s)):
    if s[i] == "A":
        l[0] += 1
    elif s[i] == "B":
        l[1] += 1
    elif s[i] == "C":
        l[2] += 1
    elif s[i] == "D":
        l[3] += 1
    elif s[i] == "E":
        l[4] += 1
    else:
        l[5] += 1
print(*l)