#ポインタの訓練になる？

n = int(input())
l = []
for i in range(n):
    a = int(input())-1
    l.append(a)
l2 = [0]*len(l)
i = 0
cnt = 0
while l2[i] == 0 and i != 1:
    l2[i] = 1
    i = l[i]
    cnt += 1
if i == 1: #i==1だと、ランプ2が光っていることになる。
    print(cnt)
else:
    print(-1)