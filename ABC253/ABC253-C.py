#TLE
q = int(input())
l = []
l_ans = []
for i in range(q):
    tmp = list(map(int,input().split()))
    if tmp[0] == 1:
        l.append(tmp[1])
    elif tmp[0] == 2:
        for i in range(tmp[2]):
            if tmp[1] in set(l):
                l.remove(tmp[1])
    elif tmp[0] == 3:
        l_ans.append(max(l) - min(l))
if len(l_ans) > 0:
    print(*l_ans,sep="\n")