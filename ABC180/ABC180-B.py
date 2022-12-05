import math
n = int(input())
l = list(map(int,input().split()))
man = 0
for i in range(n):
    man += abs(l[i])
eu = 0
for i in range(n):
    eu += l[i]*l[i]
print(man)
print(math.sqrt(eu))
for i in range(n):
    l[i] = abs(l[i])
print(max(l))