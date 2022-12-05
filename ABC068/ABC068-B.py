n = int(input())
l = []
for i in range(1,n+1):
    if i % 2 == 1:
        l.append(0)
    else:
        tmp = i
        tmp /= 2
        cnt = 1
        while tmp % 2 == 0:
            tmp /= 2
            cnt += 1
        l.append(cnt)
print(l.index(max(l))+1)