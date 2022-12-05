n = int(input())
l = []
for i in range(n):
    l.append(input())
l2 = list(set(l))
l2.sort()
d = dict(zip(l2,[0]*len(l2)+[0]))
for i in range(n):
    d[l[i]] += 1
dmax = max(d.values())
for i in d:
    if d[i] == dmax:
        print(i)