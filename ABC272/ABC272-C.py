n = int(input())
l = list(map(int,input().split()))
l.sort()
odd = []
even = []
for i in l:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
l = [-1]
if len(even) <= 1 and len(odd) <= 1:
    pass
else:
    if len(even) >= 2:
        a = even[-1] + even[-2]
        l.append(a)
    if len(odd) >= 2:
        a = odd[-1] + odd[-2]
        l.append(a)
print(max(l))