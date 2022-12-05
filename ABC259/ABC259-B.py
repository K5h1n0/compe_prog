import math
a,b,d = map(int,input().split())
c = a * math.cos(math.radians(d)) - b * math.sin(math.radians(d))
d = a * math.sin(math.radians(d)) + b * math.cos(math.radians(d))
print(c,d)