#PyPyで提出するとTLEしない
import math
n = int(input())
sum = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            sum += math.gcd(math.gcd(i,j),k)
print(sum)