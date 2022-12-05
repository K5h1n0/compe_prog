a,b = map(int,input().split())
s = input()
flg = 0
for i in range(len(s)):
    if a > 0:
        if ord("0") <= ord(str(s[i])) and ord(str(s[i])) <= ord("9"):
            a -= 1
        else:
            break
    elif a == 0 and s[i] == "-" and flg == 0:
        flg = 1
    elif a == 0 and b > 0 and flg == 1:
        if ord("0") <= ord(str(s[i])) and ord(str(s[i])) <= ord("9"):
            b -= 1
        else:
            break
    else:
        break
if a == 0 and b == 0 and flg == 1:
    print("Yes")
else:
    print("No")