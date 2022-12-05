#Otoshidama
n,y = map(int, input().split())

def kannsuu (n,y):
    for i in range(n):
        for j in  range(n-i):
            k = n - i - j
            if 10000 * i + 5000 * j + 1000 * k == y and k > 0:
                return i,j,k
    return -1,-1,-1
i,j,k=kannsuu(n,y)
print(i,j,k)