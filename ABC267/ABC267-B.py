"""
s = list(input())
ans = "No"
x1 = int(s[6])
x2 = int(s[3])
x3 = int(s[1]) + int(s[7])
x4 = int(s[0]) + int(s[4])
x5 = int(s[2]) + int(s[8])
x6 = int(s[5])
x7 = int(s[9])
if int(s[0]) == 0:
    if x2 == 0 and x1 >= 1 and x3 + x4 + x5 + x6 + x7 >= 1:
        ans = "Yes"
    if x3 == 0 and x1 + x2 >= 1 and x4 + x5 + x6 + x7 >= 1:
        ans = "Yes"
    if x4 == 0 and x1 + x2 + x3 >= 1 and x5 + x6 + x7 >= 1:
        ans = "Yes"
    if x5 == 0 and x1 + x2 + x3 + x4 >= 1 and x6 + x7 >= 1:
        ans = "Yes"
    if x6 == 0 and x1 + x2 + x3 + x4 + x5 >= 1 and x7 >= 1:
        ans = "Yes"
print(ans)
"""

s = list(input())
l = [int(s[6]),int(s[3]),int(s[1]) + int(s[7]),int(s[0]) + int(s[4]),int(s[2]) + int(s[8]),int(s[5]),int(s[9])]
ans = "No"
if int(s[0]) == 0:
    for i in range(1,len(l)-1): #左端と右端以外のレーンを見ていく
        left = 0
        right = 0
        for j in range(0,i-1): #左端から調べたいレーンより手前までのピンの本数
            left += l[j]
        for j in range(i+1,len(l)): #調べたいレーンの右隣から右端のピンの本数
            right += l[j]
        if l[i] == 0 and left >=1 and right >=1: #調べたいレーンのピンが０本かつ、左と右に1本以上立っているなら 
            ans = "Yes"
print(ans)