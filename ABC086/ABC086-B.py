import math

a,b = input().split()
n = a + b
if math.sqrt(int(n))%1 == 0:
    print("Yes")
else:
    print("No")