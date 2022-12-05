l,h = map(int,input().split())
n = int(input())
l_ans = []
for i in range(n):
    time = int(input())
    if time < l:
        l_ans.append(l-time)
    elif l <= time <= h:
        l_ans.append(0)
    elif h < time:
        l_ans.append(-1)
print(*l_ans,sep="\n")