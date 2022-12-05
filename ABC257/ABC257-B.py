n,k,q = map(int, input().split()) 
a = list(map(int, input().split()))
l = list(map(int, input().split()))
for i in range(q):
    next = a[l[i]-1] + 1
    if next not in a and a[l[i]-1] < n:
        a[l[i]-1] += 1
print(*[i for i in a if i != 0])



"""
n,k,q = map(int, input().split()) 
a = list(map(int, input().split()))
l = list(map(int, input().split()))
masu = [0] * n
for i in a:
    masu[i-1] = i
masu.sort()
masu = [i for i in masu if i != 0] 
for i in range(q):
    next = masu[l[i]-1] + 1
    if next not in masu and masu[l[i]-1] < n:
        masu[l[i]-1] += 1
print(*[i for i in masu if i != 0])
"""
"""
n,k,q = map(int, input().split()) 
a = list(map(int, input().split()))
l = list(map(int, input().split()))
masu = [0] * n
for i in a:
    masu[i-1] = i
print(masu) #メインで使っていくマス
masu.sort()
masu = [i for i in masu if i != 0] #マスの無いところを消す
print(masu)


for i in range(q):
    print(masu[l[i]-1]) #qのリストから取り出して、そこで指定された駒がどこにいるか取得
    next = masu[l[i]-1] + 1
    print(next)

    print(next not in masu)
    if next not in masu and masu[l[i]-1] < n:
        masu[l[i]-1] += 1
    print(masu)


masu1 = [0] * n
for j in masu:
    masu1[j-1] = j
print(masu1)
"""