x = int(input())
l = []
for i in range(1,100):
    for j in range(2,10):
        a = i**j 
        if a <= 1000:
            l.append(a)
l = list(set(l))
l.sort()
ans = 0
for i in range(len(l)):
    if l[i] <= x:
        ans = l[i]
print(ans)