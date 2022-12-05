n = int(input())
l = [2,1]
if n == 1:
    print(l[n])
else:
    for i in range(1,n):
        l.append(l[i-1]+l[i])
    print(l[n])