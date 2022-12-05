n = int(input())
s = list(input())
ans = ""
for i in range(len(s)):
    a = (ord(s[i])-65+n)%26
    ans += chr(a+65)
print(ans)