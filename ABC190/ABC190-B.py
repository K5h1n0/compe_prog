n,s,d = map(int, input().split())
l = []
for i in range(n):
    l.append(list(map(int,input().split())))
flg = 0
for i in range(n):
    if l[i][0] < s and l[i][1] > d:
        flg = 1
if flg == 0:
    print("No")
else:
    print("Yes")