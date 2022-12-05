a,b,c,x = map(int, input().split()) 
d = 0
if x <= a:
    d = 1
elif x > a and b >= x:
    d = c/(b-a)
print(d)