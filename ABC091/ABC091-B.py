#辞書型の扱いに慣れないとダメ

import copy

n = int(input())
s = []
for i in range(n):
    s.append(input())
s2 = copy.copy(s)
s3 = [0] * len(s2)
s4 = {}
s4.update(zip(s2,s3))

m = int(input())
t = []
for i in range(m):
    t.append(input())

for i in range(len(s)):
    s4[s[i]] += 1

for i in range(len(t)):
    if t[i] in s4:
        s4[t[i]] -= 1
print(max(0,max(s4.values())))