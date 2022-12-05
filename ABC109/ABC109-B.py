n = int(input())
a = input()
l = [a]
ans = "Yes"
for i in range(n-1):
    b = input()
    l.append(b)
    if a[-1] != b[0]:
        ans = "No"
    a = b
l2 = set(l)
if len(l) != len(l2):
    ans = "No"
print(ans)