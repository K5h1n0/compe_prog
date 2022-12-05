n = int(input())
l = list(map(int,input().split()))
now = 1
cnt = 0
for i in range(len(l)):
    if l[i] == now:
        now += 1
    else:
        cnt += 1
if cnt == len(l): #全部レンガを壊していたら-1
    print(-1)
else:
    print(cnt)