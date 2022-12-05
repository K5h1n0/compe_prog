n = int(input())
l = list(map(int,input().split()))
total = 0
for i in range(n-1):
    for j in range(i+1,n):
        total += l[i] * l[j]
print(total)