s = list(input())
t = list(input())
s.sort()
t.sort(reverse=True)
if s == t:
    print("No")
    exit()
ans = "Yes"
#このやり方思いついた。天才か？
for i in range(min(len(s),len(t))):
    if ord(s[i]) == ord(t[i]):
        flg = 1
        continue
    elif ord(s[i]) < ord(t[i]):
        flg = 0
        break
    elif ord(s[i]) > ord(t[i]):
        flg = 0
        ans = "No"
        break
if flg == 1 and len(s) > len(t):
    ans = "No"
print(ans)