o = input()
e = input()
ans = ""
for i in range(len(o)+len(e)):
    tmp = i//2
    if i % 2 == 0:
        ans += o[tmp]
    else:
        ans += e[tmp]
print(ans)