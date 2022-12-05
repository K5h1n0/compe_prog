n = int(input())
l = list(map(int,input().split()))
minimum = 100000000
for i in range(101):
    total = 0
    for j in range(n):
        total += (l[j] - i)**2
    if minimum > total:
        minimum = total
print(minimum)