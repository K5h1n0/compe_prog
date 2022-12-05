"""
n = list(input())
tmp = n[0]
flg = 0
for i in range(1,4):
    if n[i] == tmp:
        flg += 1
        if flg == 2:
            print("Yes")
            exit()
    else:
        flg = 0
        tmp = n[i]
print("No")
"""

n = list(input())
if (n[0]==n[1] and n[1]==n[2]) or (n[1]==n[2] and n[2]==n[3]):
    print("Yes")
else:
    print("No")