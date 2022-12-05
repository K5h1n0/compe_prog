l = []
zahyo = []
for i in range(9):
    tmp = list(input())
    l.append(tmp)
    for j in range(len(tmp)):
        if tmp[j] == "#":
            zahyo.append([i,j])
ans = 0
for i in range(len(zahyo)-1):
    for j in range(i+1,len(zahyo)):
        xkyori = zahyo[j][1] - zahyo[i][1]
        ykyori = zahyo[j][0] - zahyo[i][0]
        
        x3 = zahyo[j][0] - xkyori
        y3 = zahyo[j][1] + ykyori

        x4 = zahyo[i][0] - xkyori
        y4 = zahyo[i][1] + ykyori
        
        if 0 <= x3 <= 8 and 0 <= y3 <= 8 and 0 <= x4 <= 8 and 0 <= y4 <= 8 and l[x3][y3] == "#" and l[x4][y4] == "#":
            ans += 1
print(ans//2)