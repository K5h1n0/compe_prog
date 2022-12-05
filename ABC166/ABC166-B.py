n,k = map(int,input().split())
l = []
l2 = [0] + [0]*n
for i in range(k):
    tmp = int(input())
    l.append(list(map(int,input().split())))
    for j in range(tmp):
        l2[l[i][j]] += 1
l2.pop(0)
cnt = 0
for i in range(len(l2)):
    if l2[i] == 0:
        cnt += 1
print(cnt)