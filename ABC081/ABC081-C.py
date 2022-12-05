#辞書型慣れないとダメだよなあ……
import copy

n,k = map(int,input().split())
l1 = list(map(int,input().split()))
l2 = copy.copy(l1)
l2 = list(set(l2))
l3 = [0]*len(l2)
l4 = dict(zip(l2,l3))
for i in range(len(l1)):
    l4[l1[i]] += 1
ans = 0
l4 = sorted(l4.items(), key=lambda x:x[1], reverse=True)
while len(l4) > k:
    ans += l4[-1][1]
    l4.pop()
print(ans)