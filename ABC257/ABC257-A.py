a,b = map(int, input().split())
l = []
for i in range(65,91):
    for j in range(a):
        l.append(chr(i))
print(l[b-1])
