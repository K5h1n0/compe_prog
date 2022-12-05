n,x = map(int,input().split())
l = sorted(list(map(int,input().split())))
cnt = 0
for i in range(len(l)):
    if x < l[i]:
        break
    elif x >= l[i] and i <= len(l)-2:
        x -= l[i]
        cnt += 1
    elif i == len(l)-1:
        if x == l[i]:
            cnt += 1
print(cnt)