s = list(input())
l = []
for i in range(7):
    if s[i] == "a":
        l.append(0)
    elif s[i] == "t":
        l.append(1)
    elif s[i] == "c":
        l.append(2)
    elif s[i] == "o":
        l.append(3)
    elif s[i] == "d":
        l.append(4)
    elif s[i] == "e":
        l.append(5)
    elif s[i] == "r":
        l.append(6)
s2 = list("atcoder")
n = 7
cnt = 0
while n > 1:
    i = 0
    while n-1 > i:
        if s2 == s:
            break
        if s2[i] < s2[i+1]:
            w = s2[i]
            s2[i] = s2[i+1]
            s2[i+1] = w
        i += 1
        cnt += 1
        print(s2)
    n -= 1
print(cnt)