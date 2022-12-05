n = int(input())
l = list(map(int,input().split()))
total = 0
cnt = 0
for i in range(len(l)):
    if l[i] > 0:
        total += l[i]
        cnt += 1
if (total/cnt)%1 != 0:
    print(total//cnt+1)
else:
    print(total//cnt)