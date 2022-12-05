n = int(input())
l = [input() for _ in range(n)]
ans = "correct"
for i in range(n):
    for j in range(n):
        if i == j:
            pass
        elif l[i][j] == "D" and l[j][i] == "D":
            pass
        elif l[i][j] == "W" and l[j][i] == "L":
            pass
        elif l[i][j] == "L" and l[j][i] == "W":
            pass
        else:
            ans = "incorrect"
print(ans)
