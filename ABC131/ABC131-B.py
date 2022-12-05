n,r = map(int,input().split())
souwa = 0
for i in range(n):
    souwa += i+r
l = []
l2 = []
for i in range(n):
    summary = 0
    for j in range(n):
        if i == j:
            pass
        else:
            summary += j+r
    l2.append(abs(souwa-summary))
    l.append(summary)
print(l[l2.index(min(l2))])