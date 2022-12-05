n,m = map(int,input().split())
ln = []
for i in range(n):
    ln.append(list(input()))
lm = []
for i in range(m):
    lm.append(list(input()))
ans = "No"
for i in range(n-m+1):
    for j in range(n-m+1):
        #Mの方の左上が一致するか。一致したら探索を開始する。
        if lm[0][0] == ln[i][j]:
            flg = 0
            for k in range(m):
                for l in range(m):
                    if lm[k][l] == ln[i+k][j+l]:
                        flg += 1
                    else:
                        flg = 0
                        break
            if flg == m**2:
                ans = "Yes"
                break
print(ans)