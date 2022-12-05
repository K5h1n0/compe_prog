#全然簡単ではない。滅茶苦茶ややこしい。
a,b,c,x,y = map(int,input().split())
if a + b <= c*2:
    print(a*x+b*y)
else:
    if x > y:
        nokori = x - y
        total = c*y*2 + min(nokori*a,c*2*nokori)
    else:
        nokori = y - x
        total = c*x*2 + min(nokori*b,c*2*nokori)
    print(total)