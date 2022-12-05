s = input()
zen = int(s[2:])
kou = int(s[:2])
ans = "NA"
if zen == 0 or kou == 0:
    if 1 <= zen <= 12:
        ans = "YYMM"
    elif 1 <= kou <= 12:
        ans = "MMYY"
else:
    if 1 <= zen <= 12:
        if 1 <= kou <= 12:
            ans = "AMBIGUOUS"
        elif 12 < kou:
            ans = "YYMM"
    else:
        if 1 <= kou <= 12:
            ans = "MMYY"
        else:
            ans = "NA"
print(ans)