
n = int(input())
l = list(map(int,input().split()))
l2 = []
l2.append(0)
for i in range(len(l)):
    tmp = 0
    for j in range(0,i+1):
        tmp += l[j]
    l2.append(tmp%360)
l2.sort()
ans = []
for i in range(len(l2)-1,-1,-1): #この書き方は何? 1ずつ減らしていく書き方にも慣れる。
    ans.append(l2[i]-l2[i-1])
print(max(ans))