n = int(input()) 
l = [input() for _ in range(n)]
l = "".join(map(str, l))
l = list(l)
l2 = []
ma = 0
for i in range(len(l)):
    if ma < int(l[i]):
        ma = int(l[i])

l3 = [[]]
for i in range(len(l)):
    print(l)
    z = l[0]
    if str(z) == str(ma):
        print("Yes")
        print(*l)
        a = ""
        a += l[0]
        for j in range(n-1):
            a += l[-1-j]
        print(a)
        l2.append(int(a))

        b = ""
        b += l[0]
        for j in range(n-1):
            b += l[(1-n)+j]
        print(b)
        l2.append(int(b))

        c = ""
        for j in range(n):
            c += l[j*n]
        print(c)
        l2.append(int(c))

        d = ""
        d += l[0]
        for j in range(n-1):
            d += l[(n-(j+1))*n]
        print(d)
        l2.append(int(d))

        e = ""
        e += l[0]
        e += l[1]
        for j in range(n-2):
            e += l[1+(n+1)*(j+1)]
        print(e)
        l2.append(int(e))

        f = ""
        f += l[0]
        for j in range(n-1):
            f += l[1+(n+1)*(n-2-j)]
        print(f)
        l2.append(int(f))

        g = ""
        for j in range(n):
            g += l[(n-1)*j]
        print(g)
        l2.append(int(g))

        h = ""
        h += l[0]
        for j in range(n-1):
            h += l[(n-1)*(n-1-j)]
        print(h)
        l2.append(int(h))

    z = l.pop(0)
    l.append(z)
print(max(l2))
