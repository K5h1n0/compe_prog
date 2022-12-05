#WA
n,q = map(int,input().split())
s = input()
l = list(range(0,n))
ans = []
p = 0
for i in range(q):
    t,x = map(int,input().split())
    if t == 1:
        p += x
    elif t == 2:
        ans.append() #わからない。%を使うらしい
print(*ans,sep="\n")