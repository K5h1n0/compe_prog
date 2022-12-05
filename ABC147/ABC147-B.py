import copy
s = list(input())
s2 = copy.copy(s)
s2.reverse()
cnt = 0
for i in range(len(s)):
    if s[i] != s2[i]:
        cnt += 1
print(cnt//2)
