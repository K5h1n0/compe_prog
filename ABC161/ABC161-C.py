n,k = map(int,input().split())
if n%k == 0:
    print(0)
else:
    a = n%k
    minimum = 9999999999999999999
    for i in range(2):
        a = abs(a-k)
        if minimum > a:
            minimum = a
    print(minimum)