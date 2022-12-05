n = int(input())
l = []
for i in range(n):
    l.append(input())
l = list(set(l))
print(len(l))