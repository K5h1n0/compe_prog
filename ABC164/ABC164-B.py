a,b,c,d = map(int,input().split())
flg = 0
while a > 0 and c > 0 :
    if flg == 0:
        c = c - b
        flg = 1
    else:
        a = a - d
        flg = 0
if a <= 0:
    print("No")
elif c <= 0:
    print("Yes")