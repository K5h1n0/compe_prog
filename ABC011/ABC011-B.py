s = list(input())
if ord("a") <= ord(s[0]) <= ord("z"):
    s[0] = chr(ord(s[0])-32)
for i in range(1,len(s)):
        if ord("A") <= ord(s[i]) <= ord("Z"):
            s[i] = chr(ord(s[i])+32)
print(*s,sep="")