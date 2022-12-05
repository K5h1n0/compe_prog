from statistics import mode
n = int(input()) 
l = [list(map(int, input().split())) for _ in range(n-1)]
l2 =[]
if len(l) < 10:
    a = len(l)
else:
    a = 10
for i in range(a):
    l2.append(l[i][0])
    l2.append(l[i][1])
b = mode(l2)
for i in range(len(l)):
    if l[i][0] == b or l[i][1] == b:
        flg = 0
    else:
        flg = 1
        break
if flg == 0:
    print("Yes")
else:
    print("No")