l = []
for i in range(10):
    l.append(input())
flg = 0
for i in range(10):
    for j in range(10):
        if l[i][j] == "#":
            if flg == 0:
                a = i+1
                c = j+1
                flg = 1
            b = i+1
            d = j+1
print(a,b)
print(c,d)