import math

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

factorization(24) 


k = int(input())
print(factorization(k))
for i in range(0,15):
    f = math.factorial(i)
    print(f)
    l = factorization(f)
    print(l)