import math
a,b,h,m = map(int,input().split())
summ = h*60 + m
print(summ)
print("分針の角度は",m/60*360)
print("時針の角度は",summ/720*360)
mkakudo = math.radians(m/60*360)
print(mkakudo)
hkakudo = math.radians(summ/720*360)
print(hkakudo)
