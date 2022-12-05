#ちょっと余分なコードがあるかもという認識。汚い。理解度もそれほど。

n,a,b = map(int,input().split())
s = input()
tuuka = 0
maximum = a+b
ans = []
for i in range(len(s)):
    if s[i] == "c":
        ans.append("No")
    elif s[i] == "a":
        if tuuka < maximum:
            ans.append("Yes")
            tuuka += 1
        elif tuuka >= maximum:
            ans.append("No")
    elif s[i] == "b":
        if b > 0 and tuuka < maximum:
            ans.append("Yes")
            b -= 1
            tuuka += 1
        else:
            ans.append("No")
print(*ans,sep="\n")