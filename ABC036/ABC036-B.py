#2次元配列の初期化は覚える！
n = int(input())
l = []
l2 = [[""] * n for i in range(n)] #2次元配列の初期化の書き方は覚える！
for i in range(n):
    l.append(list(input()))
for i in range(n):
    for j in range(n):
        l2[j][n-i-1] = l[i][j]
for i in range(n):
    print(*l2[i],sep="")