n = int(input())
l = []
start = 0
for i in range(n):
    tmp = list(input())
    for j in range(len(tmp)):
        if int(tmp[j]) > start:
            start = int(tmp[j])
    l.append(tmp)
x = [-1,0,1,-1,1,-1,0,1]
y = [-1,-1,-1,0,0,1,1,1]
maximum = 0
for i in range(n):
    for j in range(n):
        if l[i][j] == str(start):
            #print("始点はここ",i,j)
            l2 = []
            for k in range(8):
                tmp = 0
                for m in range(n):
                    tmp *= 10
                    tmp += int(l[(i+x[k]*m)%n][(j+y[k]*m)%n])
                l2.append(tmp)
            if max(l2) > maximum:
                maximum = max(l2)
print(maximum)