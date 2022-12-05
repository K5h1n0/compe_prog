n = int(input())
s = list(input())
cnt = 0
for i in range(n-2):
    if s[i] == "A" and s[i+1] == "B" and s[i+2] == "C":
        cnt +=1
print(cnt)

"""
n = int(input())
s = list(input())
flg = 0
cnt = 0
for i in s:
    if i == "A":
        flg = 1
    elif flg == 1:
        if i == "B":
            flg = 2
        else:
            flg = 0
    elif flg == 2:
        if i == "C":
            cnt +=1
            flg = 0
        else:
            flg = 0
print(cnt)
"""