n = int(input())
l = []
for i in range(n):
    l.append(list(map(int,input().split())))
cnt = 0
for i in range(0,n-1):
    for j in range(i+1,n):
        x = l[j][0]-l[i][0]
        y = l[j][1]-l[i][1]
        a = y/x
        if a <= 1 and a >= -1:
            cnt += 1
print(cnt)