s = input()
tmp = s[0]
cnt = 1
ans = ""
for i in range(1,len(s)):
    if s[i] == tmp:
        cnt += 1
    else:
        ans = ans + tmp + str(cnt)
        cnt = 1
    tmp = s[i]
ans = ans + tmp + str(cnt)
print(ans)