n = int(input())
l = [input() for _ in range(n)]
l2 = list(set(l))
l3 = []
for i in range(len(l2)):
    l3.append(l.count(l2[i]))
max = max(l3)
print(l2[l3.index(max)])