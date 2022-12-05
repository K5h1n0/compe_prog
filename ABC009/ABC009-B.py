n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
l = list(set(l))
l.sort()
print(l[-2])