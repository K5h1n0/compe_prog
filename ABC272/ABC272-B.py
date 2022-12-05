n,m = map(int,input().split())
l = [[0 for ___ in range(n)] for ___ in range(n)]
for i in range(m):
    l2 = list(map(int,input().split()))
    sentou = l2[0]
    l2 = l2[1:]
    for j in range(sentou):
        for k in range(sentou):
            if l2[j] != l2[k]:
                l[l2[j]-1][l2[k]-1] = 1
ans = "Yes"
for i in range(len(l)):
    for j in range(len(l)):
        if i == j:
            pass
        else:
            if l[i][j] != 1:
                ans = "No"
print(ans)