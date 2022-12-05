x,k,d = map(int,input().split())
flg = 0
for i in range(k):
    if flg >= 2:
        break
    elif abs(x-d) <= abs(x+d):
        x = x-d
        flg += 1
    elif abs(x+d) < abs(x-d):
        x = x+d
        flg -= 1
    print(x)
