n = int(input())
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
maximum = 0
for i in range(0,n):
    tmp = 0
    for j in range(0,i+1):
        tmp += l1[j]    
    for j in range(i,n):
        tmp += l2[j]
    if maximum < tmp:
        maximum = tmp
print(maximum)