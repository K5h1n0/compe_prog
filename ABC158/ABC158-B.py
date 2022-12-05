#苦手な問題系
n,a,b = map(int,input().split())
blue = (n//(a+b)) * a
rem = n - ((n//(a+b)) * (a+b))
if rem > a:
    blue += a
else:
    blue += rem
print(blue)