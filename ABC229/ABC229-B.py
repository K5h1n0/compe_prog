a,b = input().split()
a = list(a)
b = list(b)
a.reverse()
b.reverse()
flg = 0
if len(a) > len(b):
    for i in range(len(b)):
        if int(a[i]) + int(b[i]) >=10:
            flg = 1
            break
else:
    for i in range(len(a)):
        if int(a[i]) + int(b[i]) >=10:
            flg = 1
            break
if flg == 0:
    print("Easy")
else:
    print("Hard")