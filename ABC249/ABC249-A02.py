A, B, C, D, E, F, X = map(int, input().split())  

t1 = 0
w1 = X

acnt = 0
ccnt = 0
Tnokyori = 0

while w1 > 0 :

    if t1 == 0:
        w1 -= A
        acnt += 1
        t1 = 1
    elif t1 == 1:
        w1 -= C
        ccnt += 1
        t1 = 0

Y = acnt * A + ccnt * C #歩いている秒数（仮）
Tnokyori = acnt * B

if X < Y:
    zettai = abs(X - Y)
    print(zettai)
    if t1 == 1:
        Tnokyori = Tnokyori - zettai * B

print(Tnokyori)
