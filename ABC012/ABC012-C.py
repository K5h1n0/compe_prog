n = int(input())
ans = []
a = []
b = []
for i in range(1,10):
    for j in range(1,10):
        ans.append(i*j)
        a.append(i)
        b.append(j)
l = []
tmp = sum(ans)-n
for i in range(len(ans)):
    if ans[i] == tmp:
        s = str(a[i]) + " " + "x" + " " + str(b[i])
        l.append(s)
l.sort()
print(*l,sep="\n")