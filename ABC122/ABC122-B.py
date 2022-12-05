s = list(input())
cnt = 0
l = [0]
for i in s:
    if i == "A" or i == "T" or i == "C" or i == "G":
        cnt += 1
    else:
        if max(l) < cnt:
            l.append(cnt)
        cnt = 0
l.append(cnt)
print(max(l))