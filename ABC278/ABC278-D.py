n = int(input())
a = list(map(int,input().split()))
q = int(input())
bo = [True]*q
l = []
now = 99999999
flg = 0
for i in range(q):
    tmp = list(map(int,input().split()))
    if flg == 0:
        if tmp[0] == 1:
            now = i
            flg = 1
        elif tmp[0] == 2:
            pass
        elif tmp[0] == 3:
            pass
    elif flg == 1:
        if tmp[0] == 1:
            bo[now] = False
            bo[i] = True
            now = i
        elif tmp[0] == 2:
            bo[i] = False
        elif tmp[0] == 3:
            for j in range(now,i+1):
                bo[j] = True
            flg = 0
    l.append(tmp)
ans = []
for i in range(q):
    if bo[i] == False:
        continue
    if l[i][0] == 1:
        a = [l[i][1]]*n
    elif l[i][0] == 2:
        a[l[i][1]-1] += l[i][2]
    elif l[i][0] == 3:
        ans.append(a[l[i][1]-1])
print(*ans,sep="\n")