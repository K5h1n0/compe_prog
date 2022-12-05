h1,w1 = map(int,input().split())
l1 = []
for i in range(h1):
    l1.append(list(map(int,input().split())))
h2,w2 = map(int,input().split())
l2 = []
for i in range(h2):
    l2.append(list(map(int,input().split())))

for i in range(h1):
    print(l1[i])
print()
ans = "No"
cnt = 0
for i in range(2 ** h1-1):
    ltate = []
    for j in range(h1):
        if ((i >> j) & 1):
            ltate.append(j)
        else:
            pass    
        for k in range(2 ** w1-1):
            lyoko = []
            for m in range(w1):
                cnt += 1
                if ((k >> m) & 1):
                    lyoko.append(m)
                else:
                    pass
        print("tate",ltate)
        print("yoko",lyoko)
        print(cnt)
