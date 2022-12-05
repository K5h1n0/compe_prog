
"""
#行けると思ったが、例えば、abbbcc、abbccccの時にWA
s = list(input())
t = list(input())
s_new = []
t_new = []
#
tmp = s[0]
s_new.append(tmp)
flg = 0
for i in range(1,len(s)):
    if s[i] != tmp:
        flg = 0
        tmp = s[i]
        s_new.append(s[i])
    elif s[i] == tmp and flg == 0:
        s_new.append(s[i])
        flg = 1
    elif s[i] == tmp and flg == 1:
        pass
#
tmp = t[0]
t_new.append(tmp)
flg = 0
for i in range(1,len(t)):
    if t[i] != tmp:
        flg = 0
        tmp = t[i]
        t_new.append(t[i])
    elif t[i] == tmp and flg == 0:
        t_new.append(t[i])
        flg = 1
    elif t[i] == tmp and flg == 1:
        pass
print(s_new)
print(t_new)
if s_new == t_new and len(s) <= len(t):
    print("Yes")
else:
    print("No")
"""