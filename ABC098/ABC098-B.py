n = int(input())
s = input()
ans = 0
for i in range(n):
    l1 = list(set(s[:i]))
    l2 = list(set(s[i:]))
    cnt = 0
    for j in range(len(l1)):
        if l1[j] in l2:
            cnt += 1
    if cnt > ans:
        ans = cnt
print(ans)

#制約がn<=100なのでできているけど、あまり良くないやり方だと思う。