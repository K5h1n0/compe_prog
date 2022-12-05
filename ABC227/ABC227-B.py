n = int(input())
s = list(map(int, input().split()))
l2 = []
l = [0] * len(s)
for i in range(1,150):
    for j in range(1, 150):
        if 4*i*j+3*i+3*j > 1000:
            pass
        else:
            l2.append(4*i*j+3*i+3*j)
l2.sort()
l2 = list(set(l2))
for i in range(n):
    if s[i] not in l2:
        l[i] = 1
print(l.count(1))