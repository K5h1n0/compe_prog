s = input()
n = int(s)
s = list(s)
for i in range(len(s)-1,-1,-1):
    s[i] = "9"
    print(*s,sep="")
print(s)