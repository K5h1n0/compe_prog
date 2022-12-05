#解説AC　このやり方じゃないとTLEだった。

n = int(input())
l2 = list(range(1,n+1))
l = list(map(int,input().split()))
l3 = list(zip(l,l2))
l3.sort(reverse=True)
for i in range(n):
    print(l3[i][1])
