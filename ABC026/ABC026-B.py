import math

n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
l.sort(reverse=True)
total = 0
for i in range(n):
    if i % 2 == 0:
        total += l[i]*l[i]*math.pi
    else:
        total -= l[i]*l[i]*math.pi
print(total)