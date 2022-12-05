n = int(input())
l = [[0 for i in range(n)] for j in range(n)] #空の二次元配列を用意
for i in range(n):
    l[i][0] = 1
    l[i][i] = 1
    j = 1
    while j < i:
        l[i][j] = l[i-1][j-1] + l[i-1][j]
        j = j + 1
    i = i + 1
for j in l:
    j = [tmp for tmp in j if tmp != 0] 
    print(*j)

"""
この2つで二次元配列の扱い方が変わる？
なんだか挙動が違う。
l = [[0]*n]*n
l = [[0 for i in range(n)] for j in range(n)]
"""