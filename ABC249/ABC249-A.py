"""

A, B, C, D, E, F, X = map(int, input().split())  

x = A+C
y = D+F
n = X // x #全体の時間で、何セット分できるか
m = X // y

print(n)
print(m)

if n == 0:
    n=1
if m == 0:
    m=1

for i in range(n):
    #Takahashiが進んだメートル
    o = A * B
o += X -  ( n * (A + C))

for j in range(m):
    #Aokiが進んだメートル
    p = D * E
p += X -  ( m * (D + F))

if o == p:
    print("Draw")
elif o > p:
    print("Takahashi")
elif o < p:
    print("Aoki")

"""

a,b,c,d,e,f,x = map(int, input().split()) 

g = a + c 
tkaisuu = x // g
if tkaisuu == 0: 
    tkyori = a * b
else:
    tamari = x - tkaisuu * g 
    if tamari >= a :
        tamari -= a
    tkyori = a * b * tkaisuu 
    tkyori =  tkyori + (b * tamari)
 
h = d + f 
akaisuu = x // h
if akaisuu == 0: 
    akyori = d * e
else:
    aamari = x - akaisuu * h
    if aamari >= d :
        aamari -= d
    akyori = d * e * akaisuu 
    akyori =  akyori + (e * aamari) 
 
if tkyori == akyori:
    print("Draw")
elif tkyori > akyori:
    print("Takahashi")
elif tkyori < akyori:
    print("Aoki")