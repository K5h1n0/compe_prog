s = input()
l1 = []
l2 = []
for i in range(len(s)):
    if i % 2 == 0:
        l1.append("0")
        l2.append("1")
    else:
        l1.append("1")
        l2.append("0")
ans1 = 0
ans2 = 0
for i in range(len(s)):
    if s[i] != l1[i]:
        ans1 += 1
    if s[i] != l2[i]:
        ans2 += 1
print(min(ans1,ans2))