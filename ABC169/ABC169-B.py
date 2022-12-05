n = int(input())
l = list(map(int,input().split()))
l.sort()
sum = l[0]
for i in range(1,n):
    sum *= l[i]
    if sum > 1000000000000000000:
        sum = -1
        break
print(sum)