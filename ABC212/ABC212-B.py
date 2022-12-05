x = input()
ans = "Strong"
flg = 0
if x[0] == x[1] == x[2] == x[3]:
    ans = "Weak"
else:
    for i in range(3):
        if int(x[i]) == int(x[i+1])-1 or (int(x[i]) == 9 and  int(x[i+1]) == 0):
            flg += 1
    if flg == 3:
        ans = "Weak"
    else:
        ans = "Strong"
print(ans)
