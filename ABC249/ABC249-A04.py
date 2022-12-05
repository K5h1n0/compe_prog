#シミュレーションして無理やりAC。スマートなやり方ではない。未だに何がコーナーケースなのか分からない。
a,b,c,d,e,f,x = map(int,input().split())
#
tkyori = 0
tyasumiflg = 0
tmpa = a
tmpc = c
#
akyori = 0
ayasumiflg = 0
tmpd = d
tmpf = f
for i in range(x):
    if tyasumiflg == 0:
        tkyori += b
        tmpa -= 1
        if tmpa == 0:
            tyasumiflg = 1
            tmpa = a
    elif tyasumiflg == 1:
        tmpc -= 1
        if tmpc == 0:
            tyasumiflg = 0
            tmpc = c
    #
    if ayasumiflg == 0:
        akyori += e
        tmpd -= 1
        if tmpd == 0:
            ayasumiflg = 1
            tmpd = d
    elif ayasumiflg == 1:
        tmpf -= 1
        if tmpf == 0:
            ayasumiflg = 0
            tmpf = f
if tkyori == akyori:
    print("Draw")
elif tkyori > akyori:
    print("Takahashi")
else:
    print("Aoki")