import copy
s = list(input())
sr = copy.copy(s)
sr.reverse()
flg = 0
if s == sr:
    flg += 1
a = s[0:(len(s)-1)//2]
ar = copy.copy(a)
ar.reverse()
if a == ar:
    flg += 1
b = s[(len(s)+3)//2-1:len(s)]
br = copy.copy(b)
br.reverse()
if b == br:
    flg += 1
if flg == 3:
    print("Yes")
else:
    print("No")