n,m = map(int,input().split())
l = []
for i in range(m):
    l.append(input().split())
hanntei = [0]*n
penalty = [0]*n
for i in range(m):
    if l[i][1] == "WA":
        if hanntei[int(l[i][0])-1] == 0:
            penalty[int(l[i][0])-1] += 1
    elif l[i][1] == "AC":
        hanntei[int(l[i][0])-1] = 1
#ACを出していない問題はペナルティを加算しないことを忘れていた
total = 0
for i in range(n):
    if hanntei[i] == 1:
        total += penalty[i]
print(sum(hanntei),total)