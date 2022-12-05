def add(x):
    y = x + k
    return y
def sub(x):
    y = x - k
    return y
k,n = map(int,input().split())
l = list(map(int,input().split()))
l2 = []
l2 = list(map(sub,l))
l2 += l
l2 += list(map(add,l))
minimum = 999999999999
for i in range(2*n+1):
    if minimum > abs(l2[i+n-1] - l2[i]):
        minimum = abs(l2[i+n-1] - l2[i])
print(minimum)