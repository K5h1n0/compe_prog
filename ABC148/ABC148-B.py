n = int(input())
s,t = input().split()
moji = ""
for i in range(n):
    moji+= s[i] + t[i]
print(moji)