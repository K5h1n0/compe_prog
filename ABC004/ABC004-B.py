l = []
for i in range(4):
    l.append(list(input().split()))
for i in range(3,-1,-1):
    for j in range(3,-1,-1):
        print(l[i][j],end=" ")
    print()