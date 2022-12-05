a,b,c,d,e,f,x = map(int, input().split()) 

g = a + c #高橋君1ターンの秒数 
tkaisuu = x // g
if tkaisuu == 0: #0の時だけ例外処理
    tkyori = a * b
else:
    tamari = x - tkaisuu * g #tamariは進むことが保証されている
    if tamari >= a :
        tamari -= a
    tkyori = a * b * tkaisuu #進むメートル*ターン数
    tkyori =  tkyori + (b * tamari) #進むメートル*余りの分

h = d + f #青木君1ターンの秒数 
akaisuu = x // h
if akaisuu == 0: #0の時だけ例外処理
    akyori = d * e
else:
    aamari = x - akaisuu * h #aamariは進むことが保証されている
    if aamari >= d :
        aamari -= d
    akyori = d * e * akaisuu #進むメートル*ターン数
    akyori =  akyori + (e * aamari) #進むメートル*余りの分

if tkyori == akyori:
    print("Draw")
elif tkyori > akyori:
    print("Takahashi")
elif tkyori < akyori:
    print("Aoki")