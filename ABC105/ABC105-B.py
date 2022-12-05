#すごく頭の悪い解答な気がする
n = int(input())
four = 0
ans = "No"
if n == 4 or n == 7:
    ans = "Yes"
else:
    while four < 100:
        four = four + 4
        seven = 0
        if four + seven == n:
            ans = "Yes"
        while seven < 100:
            seven = seven + 7
            if four + seven == n:
                ans = "Yes"
print(ans)