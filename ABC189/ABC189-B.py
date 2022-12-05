n,x = map(int, input().split())
l = []
for i in range(n):
    l.append(list(map(int,input().split())))
cnt = 0
flg = 0
for i in range(n):
    cnt += l[i][0] * l[i][1]
    if cnt > x*100 and flg == 0:
        print(i+1)
        flg = 1
        break
if flg == 0:
    print(-1)


"""
#模範解答
N,X = map(int,input().split())
s = 0
for i in range(N):
  v,p = map(int,input().split())
  s += v*p
  if s > X*100:
    print(i+1)
    exit() #←模範解答のこれが凄い。初めて知った
print(-1)  #←模範解答のこれが凄い
"""