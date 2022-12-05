n = int(input())
a = n//100
b = (n%100)//10
c = (n%100)%10
print((a+b+c)*100 + (a+b+c)*10 + (a+b+c))