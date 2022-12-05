import math
p = int(input())
l = []
for i in range(1,11):
    l.append(math.factorial(i))
l.sort(reverse=True)
l2 = [0]*10
i = 0
while p > 0:
    while l[i] <= p:
        p -= l[i]
        l2[i] += 1
    i = i + 1
print(sum(l2))