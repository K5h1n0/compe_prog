n = int(input())
s_list = set()
l2 = []
l3 = []
for i in range(n):
    s,t = input().split()
    if not s in s_list:
        s_list.add(s)
        l2.append(int(t))
        l3.append(i+1)
maximum = 0
ans = 0
for i in range(len(l2)):
    if l2[i] > maximum:
        maximum = l2[i]
        ans = l3[i]
print(ans)