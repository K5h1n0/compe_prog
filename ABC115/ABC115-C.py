n,k = map(int,input().split())
l = []
for i in range(n):
    l.append(int(input()))
l.sort()
l2 = []
l2.append(0)
tmp = l[0]
sum = 0
for i in range(1,n):
    sum+=l[i]-tmp
    l2.append(sum)
    tmp = l[i]
minimum = 999999999
for i in range(n-k+1):
    if l2[i+2]-l2[i] < minimum:
        minimum = l2[i+2]-l2[i]
print(minimum)