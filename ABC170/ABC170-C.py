x,n = map(int,input().split())
l = list(map(int,input().split()))
l.sort()
l = tuple(l)
flg = 0
if not x in l:
    print(x)
    exit()
i = 1
while flg != 1:
    if not x-i in l:
        print(x-i)
        flg = 1
        exit()
    elif not x+i in l:
        print(x+i)
        flg = 1
        exit()
    i += 1