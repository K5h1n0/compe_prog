n,m,c = map(int,input().split())
b = list(map(int,input().split()))
l = []
for i in range(n):
    l.append(list(map(int,input().split())))
cnt = 0
for i in range(n):
    total = 0
    for j in range(len(b)):
        total += l[i][j] * b[j]
    if total + c > 0:
        cnt += 1
print(cnt)