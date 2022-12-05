#二分探索らしい
n,q = map(int,input().split())
a = list(map(int,input().split()))
a.sort(reverse=True)
ans = []
for i in range(q):
    tmp = int(input())
    j = 0
    while j < len(a):
        if tmp > a[j]:
            break
        j += 1
    ans.append(j)
print(*ans,sep="\n")



"""
#便利そうな奴……？
sum(x[i] <= j for j in a) #何これ。こんなの初めて見た。
"""