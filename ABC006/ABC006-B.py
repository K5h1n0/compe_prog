n = int(input())
l = [0,0,1]
if n == 1 or n == 2:
    print(0)
else:
    for i in range(2,n):
        tmp = l[i]+l[i-1]+l[i-2]
        tmp %= 10007
        l.append(tmp)
    print(l[i])