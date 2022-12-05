a,b,k = map(int,input().split())
if a >= k:
    print(a-k,b)
else:
    if a-k+b > 0:
        print(0,a+b-k)
    else:
        print(0,0)