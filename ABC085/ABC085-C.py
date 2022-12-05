n,y = map(int,input().split())
for i in range(2000+1):
    for k in range(2000+1):
        j = (max(0,n-(10000*i + 1000*k))) // 5000
        if i * 10000 + j * 5000 + k * 1000 == y and i + j + k == n:
            print(i,j,k)
            exit()
print(-1,-1,-1)